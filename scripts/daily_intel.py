#!/usr/bin/env python3
"""
Daily Threat Intel: builds a Jekyll post from REAL security news.

How it stays honest:
  1. Pulls the last ~30 hours of items from trusted public feeds (below) and
     today's additions to CISA's Known Exploited Vulnerabilities (KEV) catalog.
  2. Gemini only sees those real items (title + feed summary). It picks the most
     important stories and summarizes them. It is told not to add facts.
  3. This script, not the AI, writes every source link and the KEV table.
  4. Any story whose id doesn't match a real item, or that mentions a CVE not in
     its source text, is thrown out.
  5. No real news, or no valid stories = no post that day.

Standard library only. Needs GEMINI_API_KEY in the environment.
"""
import datetime as dt
import email.utils
import html
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

FEEDS = [
    ("CISA Advisories", "https://www.cisa.gov/cybersecurity-advisories/all.xml"),
    ("BleepingComputer", "https://www.bleepingcomputer.com/feed/"),
    ("The Hacker News", "https://feeds.feedburner.com/TheHackersNews"),
    ("Krebs on Security", "https://krebsonsecurity.com/feed/"),
    ("SecurityWeek", "https://www.securityweek.com/feed/"),
]
KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
WINDOW_HOURS = 30
MAX_ITEMS_FOR_AI = 40
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
UA = "Mozilla/5.0 (compatible; CyberJean98-DailyIntel/2.0; +https://cyberjean98.github.io)"
CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}", re.I)
POSTS_DIR = os.environ.get("POSTS_DIR", "_posts")


def log(*a):
    print(*a, file=sys.stderr)


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def clean(text, limit=600):
    text = re.sub(r"<[^>]+>", " ", html.unescape(text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    try:
        d = email.utils.parsedate_to_datetime(s)
    except (TypeError, ValueError):
        try:
            d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d.astimezone(dt.timezone.utc)


def parse_feed(source, raw):
    """Return items from an RSS 2.0 or Atom feed."""
    items = []
    root = ET.fromstring(raw)
    atom = "{http://www.w3.org/2005/Atom}"
    for it in root.iter("item"):
        items.append({
            "source": source,
            "title": clean(it.findtext("title"), 200),
            "link": (it.findtext("link") or "").strip(),
            "date": parse_date(it.findtext("pubDate") or it.findtext("{http://purl.org/dc/elements/1.1/}date")),
            "summary": clean(it.findtext("description")),
        })
    for en in root.iter(atom + "entry"):
        link = ""
        for l in en.findall(atom + "link"):
            if l.get("rel", "alternate") == "alternate":
                link = l.get("href", "")
        items.append({
            "source": source,
            "title": clean(en.findtext(atom + "title"), 200),
            "link": link.strip(),
            "date": parse_date(en.findtext(atom + "updated") or en.findtext(atom + "published")),
            "summary": clean(en.findtext(atom + "summary") or en.findtext(atom + "content")),
        })
    return [i for i in items if i["title"] and i["link"].startswith("http")]


def gather_news(now):
    cutoff = now - dt.timedelta(hours=WINDOW_HOURS)
    news, seen = [], set()
    for source, url in FEEDS:
        try:
            items = parse_feed(source, fetch(url))
        except Exception as e:  # one bad feed shouldn't stop the run
            log(f"[warn] {source}: {e}")
            continue
        fresh = [i for i in items if i["date"] and i["date"] >= cutoff]
        log(f"[info] {source}: {len(items)} items, {len(fresh)} in the last {WINDOW_HOURS}h")
        for i in fresh:
            key = re.sub(r"\W+", "", i["title"].lower())[:80]
            if key not in seen:
                seen.add(key)
                news.append(i)
    news.sort(key=lambda i: i["date"], reverse=True)
    return news[:MAX_ITEMS_FOR_AI]


def gather_kev(now):
    try:
        data = json.loads(fetch(KEV_URL))
    except Exception as e:
        log(f"[warn] KEV: {e}")
        return []
    since = (now - dt.timedelta(days=2)).date().isoformat()
    added = [v for v in data.get("vulnerabilities", []) if v.get("dateAdded", "") >= since]
    log(f"[info] KEV: {len(added)} added since {since}")
    return added


def ask_gemini(news, api_key):
    listing = [{"id": n, "source": i["source"], "title": i["title"], "summary": i["summary"]}
               for n, i in enumerate(news)]
    prompt = (
        "You are writing a short daily threat-intel briefing for a cybersecurity analyst's blog.\n"
        "Below is a JSON list of REAL news items from security feeds, each with an id.\n\n"
        "Rules (follow exactly):\n"
        "- Choose up to 3 items that matter most to defenders (active exploitation, major breaches, "
        "critical patches, government advisories). Skip marketing, webinars and opinion pieces.\n"
        "- Use ONLY facts stated in each item's title and summary. Do not add names, numbers, dates, "
        "CVE ids, victims, attribution or details that are not in that item.\n"
        "- If the summary is thin, keep your summary short rather than guessing.\n"
        "- 'what_to_do' is general defensive advice that follows from the item (patch, rotate, monitor).\n"
        "- Do not include URLs.\n"
        "- Return JSON only, in this shape:\n"
        '{"title": "post title, under 90 characters, no date", '
        '"intro": "one sentence overview", '
        '"stories": [{"id": 0, "headline": "...", "summary": "2-3 sentences", '
        '"why_it_matters": "1-2 sentences", "what_to_do": ["...", "..."]}]}\n\n'
        "Items:\n" + json.dumps(listing, ensure_ascii=False)
    )
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"},
    }).encode()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={api_key}"
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        resp = json.loads(r.read())
    text = resp["candidates"][0]["content"]["parts"][0]["text"]
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
    return json.loads(text)


def validate(result, news):
    """Keep only stories tied to a real item, with no CVE ids the source didn't mention."""
    good = []
    for s in result.get("stories", [])[:3]:
        sid = s.get("id")
        if not isinstance(sid, int) or not 0 <= sid < len(news):
            log(f"[drop] story with unknown id {sid!r}")
            continue
        item = news[sid]
        source_text = (item["title"] + " " + item["summary"]).upper()
        written = " ".join([s.get("headline", ""), s.get("summary", ""), s.get("why_it_matters", "")]
                           + list(s.get("what_to_do", [])))
        invented = [c for c in CVE_RE.findall(written) if c.upper() not in source_text]
        if invented:
            log(f"[drop] story {sid} mentions CVEs not in its source: {invented}")
            continue
        if not s.get("headline") or not s.get("summary"):
            log(f"[drop] story {sid} is missing text")
            continue
        good.append((s, item))
    return good


def md_escape(s):
    return s.replace("|", "\\|").replace("\n", " ").strip()


def render(today, result, stories, kev):
    title = (result.get("title") or "Daily Threat Intel").replace('"', "'").strip()[:100]
    sources_used = sorted({item["source"] for _, item in stories} | ({"CISA KEV"} if kev else set()))
    out = ["---", "layout: post", f'title: "{title}"', f"date: {today}", "categories: [threat-intel]",
           f"sources: [{', '.join(sources_used)}]", "---", ""]
    if result.get("intro"):
        out += [result["intro"].strip(), ""]
    for s, item in stories:
        published = item["date"].astimezone(dt.timezone(dt.timedelta(hours=-5))).strftime("%b %d, %Y")
        out += [f"### {s['headline'].strip()}", "", s["summary"].strip(), ""]
        if s.get("why_it_matters"):
            out += [f"**Why it matters:** {s['why_it_matters'].strip()}", ""]
        todo = [t.strip() for t in s.get("what_to_do", []) if t.strip()]
        if todo:
            out += ["**What to do:**", ""] + [f"- {t}" for t in todo] + [""]
        out += [f"*Source: [{md_escape(item['title'])}]({item['link']}), {item['source']}, {published}*", ""]
    if kev:
        out += ["### Newly added to CISA's Known Exploited Vulnerabilities catalog", "",
                "These are confirmed to be exploited in the wild. Federal agencies must patch by the due date, "
                "and everyone else should treat them as urgent.", "",
                "| CVE | Vendor / product | Vulnerability | Patch by |", "| --- | --- | --- | --- |"]
        for v in kev[:15]:
            cve = v.get("cveID", "")
            out.append(f"| [{cve}](https://nvd.nist.gov/vuln/detail/{cve}) | "
                       f"{md_escape(v.get('vendorProject', ''))} {md_escape(v.get('product', ''))} | "
                       f"{md_escape(v.get('vulnerabilityName', ''))} | {v.get('dueDate', '')} |")
        if len(kev) > 15:
            out.append(f"\n*Plus {len(kev) - 15} more in the [full KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).*")
        out.append("")
    out += ["---", "",
            f"*How this briefing is made: an automated pipeline pulls the last {WINDOW_HOURS} hours of public feeds "
            f"({', '.join(n for n, _ in FEEDS)}, and the CISA KEV catalog). Gemini summarizes only what those "
            "articles' feed summaries say, and every story links to its original source. Read the source before acting on it.*",
            ""]
    return "\n".join(out)


def main():
    now = dt.datetime.now(dt.timezone.utc)
    today = now.astimezone(dt.timezone(dt.timedelta(hours=-5))).date().isoformat()
    path = os.path.join(POSTS_DIR, f"{today}-daily-intel.md")
    if os.path.exists(path):
        log(f"[skip] {path} already exists")
        return 0
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        log("[error] GEMINI_API_KEY is not set")
        return 1

    news = gather_news(now)
    kev = gather_kev(now)
    if not news:
        log("[skip] no fresh news from any feed, so no post today")
        return 0

    try:
        result = ask_gemini(news, api_key)
    except Exception as e:
        log(f"[error] Gemini request failed: {e}")
        return 1
    stories = validate(result, news)
    if not stories:
        log("[skip] no story passed validation, so no post today")
        return 0

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(render(today, result, stories, kev))
    log(f"[done] wrote {path} with {len(stories)} stories and {len(kev)} KEV entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
