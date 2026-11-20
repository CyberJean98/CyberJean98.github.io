---
layout: post
title: "Building in Public: Design Systems, WordPress Themes, and Catching My Own AI Making Things Up"
date: 2026-11-19
---

This week I set out to build a web design portfolio for Upwork. Along the way I learned a professional design process, shipped three WordPress themes, and found out that my own automated news agent had been publishing invented stories for months. Here's what I built and what I learned.

### 1. A design taste playbook

Before building anything, I wrote down *how* to make design decisions. I already use [Impeccable](https://impeccable.style) with Claude for the build-level rules (type, spacing, accessibility). What was missing was the layer above that: deciding what a site should feel like and why.

The playbook covers:

- **Six style directions** (Warm Local, Editorial, Clean Pro, Bold Brutal, Technical Dark, Soft Modern), each with type, color, layout and what to avoid
- **Which direction fits which client**: restaurants, contractors, security firms, online stores
- **Ten discovery questions** for a first client call, ending in a one-line brief: *"This site should feel ___ to ___, unlike ___."*
- **A taste review checklist** to run before a client sees anything, like the "logo swap test": if a competitor's logo would work on your design, it's too generic

I also turned it into a reusable Claude skill, so every new site starts from the same process.

### 2. Three concept sites, built the way a real studio does it

My mentor Jeremy Anderson showed me how his web company works. Every site goes through the same pipeline, and each step is the reference for the next:

**Design system → Brand book → HTML example → WordPress theme**

I built three fictional businesses this way, one per style direction:

| Site | Direction | Signature element |
| --- | --- | --- |
| Brasa, a wood-fired restaurant | Warm Local | An oven-shaped "Tonight from the oven" menu card |
| Northbound Roofing, a Central MA contractor | Clean Pro | A copper-topped inspection form and a 22-town service list |
| Lockline Security, a small-business security firm | Technical Dark | A sample security report right in the hero |

Each one has a design system (colors, type, spacing, components, with every color pair checked for WCAG contrast), a brand book (voice, logo rules, do's and don'ts), a hand-built HTML page, and a **WordPress block theme**. I tested the themes on a real WordPress install with no PHP errors and no broken blocks in the Site Editor, then ran them myself in Local WP.

**Lesson:** writing the design system and brand book first made the theme much easier to build, because every decision was already made. That's exactly what Jeremy told me would happen.

[See the sites](https://cyberjean98.github.io/web-development-portfolio/) · [Code, brand books and themes](https://github.com/CyberJean98/web-development-portfolio)

### 3. My news agent was inventing the news

This site has a GitHub Actions agent that posts a daily threat briefing. When I went to clean up the site, I found two problems.

First, it had silently stopped working on November 10 because its access token expired. Second, and much worse, **every post it had ever written was made up.** The agent asked Gemini for "today's top cybersecurity news," but Gemini had no internet access in that request, so it invented stories. Some posts even admitted it: one described a breach at "NebulaCloud (fictional)" and a vulnerability numbered "CVE-2026-XXXX." None of the 189 posts linked to a real source.

For someone trying to get into a SOC, publishing fake threat intel is about the worst look possible. So I deleted all 189 posts and rebuilt the agent:

- It pulls the last 30 hours of real stories from **CISA, BleepingComputer, The Hacker News, Krebs on Security and SecurityWeek**, plus new entries in **CISA's Known Exploited Vulnerabilities** catalog.
- Gemini only sees those real headlines and summaries, and is told not to add facts.
- **The code, not the AI, writes every source link.** Any story that doesn't match a real article, or mentions a CVE its source never named, gets thrown out. I tested this with a fake AI response that tried both, and both were caught.
- No real news means no post that day.
- It now uses GitHub's built-in token with least-privilege permissions, so there's no personal key to expire.

**Lesson:** AI output needs the same treatment as any untrusted input. Validate it against a source of truth before it goes anywhere public. That's a security habit, not just a coding one.

[Read the briefings](https://cyberjean98.github.io/intel/) · [Pipeline code](https://github.com/CyberJean98/CyberJean98.github.io/blob/main/scripts/daily_intel.py)

### 4. Fixing this site

The cleanup turned up a few embarrassing bugs:

- The settings file was named `config.yml` instead of `_config.yml`, so Jekyll ignored it. The site had **no navigation menu**, and the browser tab showed my repo description, typo included.
- Three PDF links (a certificate, an incident report and a Wireshark log) pointed to file names that didn't exist.
- Two project links went to repos that were no longer public.

I fixed all of them and redesigned the site so my projects and certifications come first and the news feed comes after.

### What I'm taking away

1. **A process beats talent on a deadline.** Design system first, then brand book, then build.
2. **Verify everything automated.** My agent ran "successfully" every day while publishing fiction.
3. **Check your own work like an attacker would.** Broken links, ignored config files and expired tokens are the kind of small failures that add up.

I built all of this with help from Claude. Next up: putting the web portfolio on Upwork and getting back to Security+.
