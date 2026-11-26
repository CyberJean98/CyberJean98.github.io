---
layout: post
title: "Daily Threat Brief: CISA KEVs, 1Password Breach, GeoServer Exploitation"
date: 2026-11-26
categories: [threat-intel]
sources: [BleepingComputer, CISA KEV, SecurityWeek, The Hacker News]
---

Today's briefing highlights critical government advisories, a significant data breach, and active exploitation of newly disclosed vulnerabilities.

### Hackers Exploit 10 Vulnerabilities Across Mitel, Juniper, Vates, and Danfoss Products

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added 10 security flaws to its Known Exploited Vulnerabilities (KEV) catalog. These include five vulnerabilities impacting Mitel MiCollab that were disclosed last week, alongside flaws in Juniper, Vates, and Danfoss products.

**Why it matters:** CISA has issued an advisory regarding multiple actively exploited vulnerabilities in various products, indicating a high risk to organizations using these systems. This includes critical flaws in Mitel MiCollab, Juniper, Vates, and Danfoss products.

**What to do:**

- Review CISA's KEV catalog for affected products
- Apply patches and updates immediately for listed vulnerabilities
- Monitor systems for signs of compromise

*Source: [Hackers Exploit 10 Vulnerabilities Across Mitel, Juniper, Vates, and Danfoss Products](https://thehackernews.com/2026/11/hackers-exploit-10-vulnerabilities.html), The Hacker News, Nov 26, 2026*

### 1Password customer data stolen after employee GitHub account breach

1Password has disclosed a data breach after an employee's corporate GitHub account was hacked. This compromise was used to deploy malicious code to the company's backend services to steal customer data.

**Why it matters:** A major password management service disclosed a data breach where an employee's corporate GitHub account was compromised. Attackers used this access to deploy malicious code to backend services and steal customer data, emphasizing the importance of securing developer tools and supply chains.

**What to do:**

- Review access logs for unusual activity
- Enforce strong authentication for all employee accounts
- Implement supply chain security measures
- Rotate credentials for affected services

*Source: [1Password customer data stolen after employee GitHub account breach](https://www.bleepingcomputer.com/news/security/1password-customer-data-stolen-after-employee-github-account-breach/), BleepingComputer, Nov 25, 2026*

### Two Newly Disclosed GeoServer Vulnerabilities Under Attack

Attackers are probing GeoServer instances for two high-severity flaws. These vulnerabilities can be chained with other bugs for unauthenticated remote code execution.

**Why it matters:** Two newly disclosed high-severity vulnerabilities in GeoServer are actively being exploited by attackers. These flaws can be chained to achieve unauthenticated remote code execution, posing a significant risk to affected systems.

**What to do:**

- Identify and patch all GeoServer instances immediately
- Monitor network traffic for signs of exploitation attempts
- Review access controls for GeoServer deployments

*Source: [Two Newly Disclosed GeoServer Vulnerabilities Under Attack](https://www.securityweek.com/two-newly-disclosed-geoserver-vulnerabilities-under-attack/), SecurityWeek, Nov 25, 2026*

### Newly added to CISA's Known Exploited Vulnerabilities catalog

These are confirmed to be exploited in the wild. Federal agencies must patch by the due date, and everyone else should treat them as urgent.

| CVE | Vendor / product | Vulnerability | Patch by |
| --- | --- | --- | --- |
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
| [CVE-2026-132224](https://nvd.nist.gov/vuln/detail/CVE-2026-132224) | Optimizely Web Experimentation | Optimizely Web Experimentation External Control of Critical State Data Vulnerability | 2026-11-27 |
| [CVE-2026-131914](https://nvd.nist.gov/vuln/detail/CVE-2026-131914) | Idunno AntiCsrf | Idunno AntiCsrf Deserialization of Untrusted Data Vulnerability | 2026-11-27 |
| [CVE-2026-132165](https://nvd.nist.gov/vuln/detail/CVE-2026-132165) | Drupal Core | Drupal Core Remote Code Execution Vulnerability | 2026-11-27 |

---

*How this briefing is made: an automated pipeline pulls the last 30 hours of public feeds (CISA Advisories, BleepingComputer, The Hacker News, Krebs on Security, SecurityWeek, and the CISA KEV catalog). Gemini summarizes only what those articles' feed summaries say, and every story links to its original source. Read the source before acting on it.*
