---
layout: post
title: "Daily Threat Briefing: Critical Patches, Major Breaches, and Security Server Compromises"
date: 2026-11-24
categories: [threat-intel]
sources: [BleepingComputer, CISA KEV, SecurityWeek, The Hacker News]
---

Today's briefing highlights urgent patching needs for critical vulnerabilities, significant data breaches, and active exploitation campaigns targeting security infrastructure.

### VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After Zero-Day Exploitation

Broadcom has released patches for 23 vulnerabilities affecting VMware ESX, vCenter, Workstation, Fusion, and Avi Load Balancer. Among these is a critical authentication bypass flaw in the VMware Directory Service, rated 9.8 on the CVSS scoring system, which was discovered after zero-day exploitation.

**Why it matters:** This critical authentication bypass vulnerability affects widely used VMware products, including vCenter, and has been exploited as a zero-day. Applying the patches is crucial to prevent unauthorized access.

**What to do:**

- Apply patches immediately
- Review access logs for suspicious activity

*Source: [VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After Zero-Day Exploitation](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html), The Hacker News, Nov 24, 2026*

### 1.5 Million Impacted by Data Breach at South Korean Electric Company KEPCO

Hackers stole personal information from the customer portal and supplier relationship management platform of South Korean electric company KEPCO. This data breach impacted 1.5 million individuals.

**Why it matters:** A major data breach at an electric company can have significant implications for customer privacy and broader security. The exposure of personal information for 1.5 million individuals is a substantial incident.

**What to do:**

- Monitor for unusual activity
- Implement strong access controls
- Review third-party vendor security

*Source: [1.5 Million Impacted by Data Breach at South Korean Electric Company KEPCO](https://www.securityweek.com/1-5-million-impacted-by-data-breach-at-south-korean-electric-company-kepco/), SecurityWeek, Nov 24, 2026*

### Hackers compromise Check Point Servers in 22 organizations

Threat actors have exploited multiple vulnerabilities to compromise two dozen Check Point Security management servers. This ongoing campaign is targeting 22 organizations.

**Why it matters:** The compromise of security management servers is highly critical as it can provide attackers with deep access and control over an organization's security infrastructure. This ongoing campaign affects multiple organizations, indicating a widespread threat.

**What to do:**

- Patch Check Point servers
- Review server logs for compromise indicators
- Implement network segmentation

*Source: [Hackers compromise Check Point Servers in 22 organizations](https://www.bleepingcomputer.com/news/security/hackers-compromise-check-point-servers-in-22-organizations/), BleepingComputer, Nov 24, 2026*

### Newly added to CISA's Known Exploited Vulnerabilities catalog

These are confirmed to be exploited in the wild. Federal agencies must patch by the due date, and everyone else should treat them as urgent.

| CVE | Vendor / product | Vulnerability | Patch by |
| --- | --- | --- | --- |
| [CVE-2026-132224](https://nvd.nist.gov/vuln/detail/CVE-2026-132224) | Optimizely Web Experimentation | Optimizely Web Experimentation External Control of Critical State Data Vulnerability | 2026-11-27 |
| [CVE-2026-131914](https://nvd.nist.gov/vuln/detail/CVE-2026-131914) | Idunno AntiCsrf | Idunno AntiCsrf Deserialization of Untrusted Data Vulnerability | 2026-11-27 |
| [CVE-2026-132165](https://nvd.nist.gov/vuln/detail/CVE-2026-132165) | Drupal Core | Drupal Core Remote Code Execution Vulnerability | 2026-11-27 |
| [CVE-2026-133968](https://nvd.nist.gov/vuln/detail/CVE-2026-133968) | Project MONAI MONAI Label | Project MONAI MONAI Label Path Traversal Vulnerability | 2026-11-26 |
| [CVE-2026-134624](https://nvd.nist.gov/vuln/detail/CVE-2026-134624) | N-able MailAssure | N-able MailAssure (SpamExperts) Server-Side Request Forgery (SSRF) Vulnerability | 2026-11-26 |

---

*How this briefing is made: an automated pipeline pulls the last 30 hours of public feeds (CISA Advisories, BleepingComputer, The Hacker News, Krebs on Security, SecurityWeek, and the CISA KEV catalog). Gemini summarizes only what those articles' feed summaries say, and every story links to its original source. Read the source before acting on it.*
