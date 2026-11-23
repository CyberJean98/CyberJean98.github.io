---
layout: post
title: "Threat Brief: Azure, ScreenConnect, and CISA-Flagged Exploits"
date: 2026-11-23
categories: [threat-intel]
sources: [BleepingComputer, CISA Advisories, CISA KEV, The Hacker News]
---

Today's briefing highlights active exploitation of critical vulnerabilities in cloud services and MSP tools, alongside new CISA advisories for known exploited flaws.

### Microsoft Azure flaw exploited to steal customers' API credentials

Microsoft is warning customers that a security vulnerability in Azure API Management (APIM) Classic tiers was exploited to steal stored API credentials, with Norwegian authorities linking the flaw to cyberattacks against energy companies.

**Why it matters:** A critical vulnerability in Microsoft Azure API Management Classic tiers has been actively exploited to steal API credentials, with links to cyberattacks against energy companies, posing a significant risk to cloud security.

**What to do:**

- Review Azure API Management configurations
- Rotate API credentials
- Monitor for suspicious activity

*Source: [Microsoft Azure flaw exploited to steal customers' API credentials](https://www.bleepingcomputer.com/news/security/microsoft-azure-flaw-exploited-to-steal-customers-api-credentials/), BleepingComputer, Nov 23, 2026*

### Hackers Exploit Critical ScreenConnect Flaw to Hijack MSP Technician PCs Without Warning

Threat actors are exploiting a now-patched security flaw in ConnectWise ScreenConnect to target managed service provider (MSP) servers. The critical ScreenConnect client flaw allows a guest to transfer and execute a malicious payload on a connecting technician's host.

**Why it matters:** A critical, actively exploited vulnerability in ConnectWise ScreenConnect allows attackers to hijack MSP technician PCs, enabling malicious payload execution and posing a severe supply chain risk to organizations relying on MSPs.

**What to do:**

- Patch ConnectWise ScreenConnect immediately
- Review logs for signs of compromise
- Implement strong endpoint detection and response

*Source: [Hackers Exploit Critical ScreenConnect Flaw to Hijack MSP Technician PCs Without Warning](https://thehackernews.com/2026/11/hackers-exploit-critical-screenconnect.html), The Hacker News, Nov 23, 2026*

### CISA Adds Two Known Exploited Vulnerabilities to Catalog

CISA has added two new vulnerabilities to its Known Exploited Vulnerabilities (KEV) Catalog, based on evidence of active exploitation. These include a Project MONAI MONAI Label Path Traversal Vulnerability and an N-able Mail Assure (SpamExperts) Server-Side Request Forgery (SSRF) Vulnerability.

**Why it matters:** CISA has issued an advisory for two actively exploited vulnerabilities, a Project MONAI path traversal flaw and an N-able Mail Assure SSRF vulnerability, which are frequent attack vectors and pose significant risks.

**What to do:**

- Patch Project MONAI Label and N-able Mail Assure
- Review CISA KEV catalog regularly
- Prioritize security updates for known exploited vulnerabilities

*Source: [CISA Adds Two Known Exploited Vulnerabilities to Catalog](https://www.cisa.gov/news-events/alerts/2026/11/23/cisa-adds-two-known-exploited-vulnerabilities-catalog), CISA Advisories, Nov 23, 2026*

### Newly added to CISA's Known Exploited Vulnerabilities catalog

These are confirmed to be exploited in the wild. Federal agencies must patch by the due date, and everyone else should treat them as urgent.

| CVE | Vendor / product | Vulnerability | Patch by |
| --- | --- | --- | --- |
| [CVE-2026-133968](https://nvd.nist.gov/vuln/detail/CVE-2026-133968) | Project MONAI MONAI Label | Project MONAI MONAI Label Path Traversal Vulnerability | 2026-11-26 |
| [CVE-2026-134624](https://nvd.nist.gov/vuln/detail/CVE-2026-134624) | N-able MailAssure | N-able MailAssure (SpamExperts) Server-Side Request Forgery (SSRF) Vulnerability | 2026-11-26 |

---

*How this briefing is made: an automated pipeline pulls the last 30 hours of public feeds (CISA Advisories, BleepingComputer, The Hacker News, Krebs on Security, SecurityWeek, and the CISA KEV catalog). Gemini summarizes only what those articles' feed summaries say, and every story links to its original source. Read the source before acting on it.*
