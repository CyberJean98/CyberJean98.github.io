---
layout: post
title: "Daily Threat Brief: Zero-Days, Active Exploitation, and Major Breaches"
date: 2026-11-27
categories: [threat-intel]
sources: [BleepingComputer, CISA KEV, SecurityWeek, The Hacker News]
---

Today's briefing highlights critical vulnerabilities under active exploitation, a significant software supply chain compromise, and a major vendor cyberattack.

### Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access

Details have emerged about a new zero-day vulnerability in Cacti, an open-source network monitoring tool, that could be exploited to achieve remote code execution. The proof-of-concept (PoC) exploit allows command execution as the Cacti server from an unauthenticated HTTP session.

**Why it matters:** This is a critical zero-day vulnerability in a widely used network monitoring tool, with a publicly available proof-of-concept exploit. Unauthenticated attackers can achieve remote code execution, posing a severe risk to vulnerable systems.

**What to do:**

- Monitor vendor advisories for patches
- Apply patches immediately upon release
- Restrict network access to Cacti instances

*Source: [Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access](https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html), The Hacker News, Nov 27, 2026*

### Drupal warns of new site takeover flaw exploited in attacks

The Drupal security team says attackers are exploiting a second critical vulnerability that lets them breach and hijack unpatched websites. This flaw allows for site takeover.

**Why it matters:** A critical vulnerability in Drupal is actively being exploited by attackers to take over websites. This represents an immediate and severe threat to organizations using unpatched Drupal installations.

**What to do:**

- Apply available security updates for Drupal
- Monitor website logs for suspicious activity
- Review access controls for Drupal installations

*Source: [Drupal warns of new site takeover flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/drupal-warns-of-new-access-bypass-flaw-exploited-in-attacks/), BleepingComputer, Nov 27, 2026*

### SAP Confirms Cyberattack, Source Code Reportedly Compromised

SAP has detected suspicious activity on GitHub, where hackers reportedly used stolen employee tokens to copy and alter source code. SAP confirmed a cyberattack.

**Why it matters:** A major software vendor, SAP, has confirmed a cyberattack involving the compromise of source code via stolen employee tokens. This incident highlights supply chain risks and the potential for widespread impact on customers.

**What to do:**

- Rotate employee tokens and credentials
- Implement strong access controls for code repositories
- Monitor for suspicious activity in development environments

*Source: [SAP Confirms Cyberattack, Source Code Reportedly Compromised](https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/), SecurityWeek, Nov 27, 2026*

### Newly added to CISA's Known Exploited Vulnerabilities catalog

These are confirmed to be exploited in the wild. Federal agencies must patch by the due date, and everyone else should treat them as urgent.

| CVE | Vendor / product | Vulnerability | Patch by |
| --- | --- | --- | --- |
| [CVE-2026-120705](https://nvd.nist.gov/vuln/detail/CVE-2026-120705) | OSGeo GeoServer | OSGeo GeoServer XML Injection Vulnerability | 2026-11-30 |
| [CVE-2026-129243](https://nvd.nist.gov/vuln/detail/CVE-2026-129243) | OSGeo GeoServer | OSGeo GeoServer Incorrect Authorization Vulnerability | 2026-11-30 |
| [CVE-2026-136716](https://nvd.nist.gov/vuln/detail/CVE-2026-136716) | Drupal Core | Drupal Core Improper Check for Unusual or Exceptional Conditions Vulnerability | 2026-11-30 |
| [CVE-2026-103406](https://nvd.nist.gov/vuln/detail/CVE-2026-103406) | Hewlett Packard Enterprise (HPE) Juniper Session Smart Conductor and Session Smart Router | Hewlett Packard Enterprise (HPE) Juniper Session Smart Conductor and Session Smart Router OS Command Injection Vulnerability | 2026-11-28 |
| [CVE-2026-133469](https://nvd.nist.gov/vuln/detail/CVE-2026-133469) | Vates Xen Orchestra | Vates Xen Orchestra Improper Validation of Specified Type of Input Vulnerability | 2026-11-28 |
| [CVE-2025-41450](https://nvd.nist.gov/vuln/detail/CVE-2025-41450) | Danfoss AK-SM 800A Series | Danfoss AK-SM 800A Series Improper Authentication Vulnerability | 2026-12-09 |
| [CVE-2023-25914](https://nvd.nist.gov/vuln/detail/CVE-2023-25914) | Danfoss AK-SM 800A Series | Danfoss AK-SM 800A Series Path Traversal Vulnerability | 2026-11-28 |
| [CVE-2023-25915](https://nvd.nist.gov/vuln/detail/CVE-2023-25915) | Danfoss AK-SM 800A Series | Danfoss AK-SM 800A Series Improper Input Validation Vulnerability | 2026-11-28 |
| [CVE-2026-133324](https://nvd.nist.gov/vuln/detail/CVE-2026-133324) | Mitel MiCollab | Mitel MiCollab Not Failing Securely Vulnerability | 2026-11-28 |
| [CVE-2026-133275](https://nvd.nist.gov/vuln/detail/CVE-2026-133275) | Mitel MiCollab | Mitel MiCollab Unrestricted Upload of File with Dangerous Type Vulnerability | 2026-11-28 |
| [CVE-2026-133311](https://nvd.nist.gov/vuln/detail/CVE-2026-133311) | Mitel MiCollab | Mitel MiCollab Weak Authentication Vulnerability | 2026-12-09 |
| [CVE-2026-133303](https://nvd.nist.gov/vuln/detail/CVE-2026-133303) | Mitel MiCollab | Mitel MiCollab XML Injection Vulnerability | 2026-11-28 |
| [CVE-2026-133323](https://nvd.nist.gov/vuln/detail/CVE-2026-133323) | Mitel MiCollab | Mitel MiCollab OS Command Injection Vulnerability | 2026-11-28 |

---

*How this briefing is made: an automated pipeline pulls the last 30 hours of public feeds (CISA Advisories, BleepingComputer, The Hacker News, Krebs on Security, SecurityWeek, and the CISA KEV catalog). Gemini summarizes only what those articles' feed summaries say, and every story links to its original source. Read the source before acting on it.*
