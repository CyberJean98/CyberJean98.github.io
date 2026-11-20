# cyberjean98.github.io

Portfolio of **Jean Berrios-Marquez**, an entry-level SOC analyst, U.S. Navy veteran and builder of secure websites in Worcester, MA.

**Live site:** https://cyberjean98.github.io

## What's here

| Page | What it shows |
| --- | --- |
| [Home](https://cyberjean98.github.io/) | Career path, certifications, featured work, latest threat intel |
| [Projects](https://cyberjean98.github.io/projects/) | Home SOC lab (Wazuh), SOC ticketing console, Pwnagotchi, SYN flood incident report, threat-intel pipeline, WordPress work |
| [Web design](https://cyberjean98.github.io/web/) | Services for small businesses, example sites, process and a free quote |
| [Certifications](https://cyberjean98.github.io/certs/) | Google Cybersecurity Certificate, Forage job simulations, Security+ and TryHackMe progress, with PDFs |
| [Threat intel](https://cyberjean98.github.io/intel/) | A sourced daily briefing, generated automatically |

## Daily threat-intel pipeline

[`scripts/daily_intel.py`](scripts/daily_intel.py), run every morning by [`.github/workflows/daily-news.yml`](.github/workflows/daily-news.yml):

1. Pulls the last 30 hours from CISA, BleepingComputer, The Hacker News, Krebs on Security and SecurityWeek, plus new CISA Known Exploited Vulnerabilities entries.
2. Gemini picks and summarizes up to three stories, using only those real items.
3. The script writes every source link itself and drops any story that doesn't match a real item or mentions a CVE its source doesn't.
4. No real news means no post. The workflow uses the built-in `GITHUB_TOKEN`, so there's no personal access token to expire.

An earlier version asked the AI for "today's news" with no internet access, and it invented stories. Those 189 posts were removed and the pipeline was rebuilt around real sources and validation.

## SOC ticketing console

A ticketing system built from scratch: a FastAPI backend with a Wazuh alert webhook, and a static frontend served at [`/ticketing/`](https://cyberjean98.github.io/ticketing/). See [`ticketing-backend/README.md`](ticketing-backend/README.md).

## Built with

Jekyll on GitHub Pages, with custom layouts and CSS (no theme). Fonts: Sora and Hanken Grotesk.

## Related

- [Web development portfolio](https://github.com/CyberJean98/web-development-portfolio): concept sites, brand books and WordPress block themes
- [JAT Site Shield](https://github.com/CptNope/JAT-Site-Shield) and [JAT Shell Scanner](https://github.com/CptNope/JAT-Shell-Scanner): Spanish translations (650+ strings) shipped in versions 1.1.1 and 1.7.1; credited contributor on WordPress.org

Contact: jeanberrios53@gmail.com · [LinkedIn](https://www.linkedin.com/in/jean-berrios-marquez-2617a73b2)
