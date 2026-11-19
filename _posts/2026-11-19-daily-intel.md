---
layout: post
title: "Daily Threat Brief: VMware Zero-Day, CISA KEVs, and Critical PHP Patches"
date: 2026-11-19
categories: [threat-intel]
sources: [BleepingComputer, CISA KEV, SecurityWeek, The Hacker News]
---

Today's briefing highlights active exploitation of a VMware zero-day, CISA's warning on multiple exploited vulnerabilities, and urgent patches for critical PHP flaws.

### Newly Patched VMware vCenter Flaw Exploited as Zero-Day by Chinese APT

Google says a China-linked espionage group exploited a critical VMware vCenter authentication bypass before Broadcom released a patch. This zero-day exploitation was confirmed by security researchers.

**Why it matters:** This is a critical zero-day vulnerability in VMware vCenter that was actively exploited by an espionage group before a patch was available, posing a significant threat to enterprise environments.

**What to do:**

- Apply patches immediately
- Monitor vCenter environments for suspicious activity

*Source: [Newly Patched VMware vCenter Flaw Exploited as Zero-Day by Chinese APT](https://www.securityweek.com/newly-patched-vmware-vcenter-flaw-exploited-as-zero-day-by-chinese-apt/), SecurityWeek, Nov 19, 2026*

### CISA Warns of 4 Exploited Flaws Linked to Ransomware, Cryptomining, and LLMjacking Attacks

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added four vulnerabilities impacting Synology DiskStation Manager (DSM), BerriAI LiteLLM, Apache Axis, and Vanderbilt University Research Electronic Data Capture (REDCap) to its Known Exploited Vulnerabilities (KEV) catalog. This addition cites evidence of active exploitation for these flaws.

**Why it matters:** CISA has issued a warning about multiple vulnerabilities across various products that are actively being exploited in the wild, including for ransomware and cryptomining, indicating immediate and widespread threats.

**What to do:**

- Review CISA's KEV catalog
- Apply patches for affected products
- Monitor for signs of compromise

*Source: [CISA Warns of 4 Exploited Flaws Linked to Ransomware, Cryptomining, and LLMjacking Attacks](https://thehackernews.com/2026/11/cisa-warns-of-4-exploited-flaws-linked.html), The Hacker News, Nov 19, 2026*

### PHP security updates fix 18 flaws, including critical RCE bugs

The PHP development team released security updates addressing 18 vulnerabilities. These updates include fixes for critical flaws that could allow unauthenticated attackers to remotely execute code on vulnerable servers.

**Why it matters:** Critical security updates for PHP address numerous vulnerabilities, including remote code execution flaws that could allow unauthenticated attackers to compromise servers running the widely used scripting language.

**What to do:**

- Apply PHP security updates immediately
- Verify PHP installations are up-to-date

*Source: [PHP security updates fix 18 flaws, including critical RCE bugs](https://www.bleepingcomputer.com/news/security/php-security-updates-fix-18-flaws-including-critical-rce-bugs/), BleepingComputer, Nov 19, 2026*

### Newly added to CISA's Known Exploited Vulnerabilities catalog

These are confirmed to be exploited in the wild. Federal agencies must patch by the due date, and everyone else should treat them as urgent.

| CVE | Vendor / product | Vulnerability | Patch by |
| --- | --- | --- | --- |
| [CVE-2024-10441](https://nvd.nist.gov/vuln/detail/CVE-2024-10441) | Synology DiskStation Manager (DSM) | Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability | 2026-11-21 |
| [CVE-2026-40217](https://nvd.nist.gov/vuln/detail/CVE-2026-40217) | BerriAI LiteLLM | BerriAI LiteLLM Unprotected Alternate Channel Vulnerability | 2026-12-02 |
| [CVE-2026-90817](https://nvd.nist.gov/vuln/detail/CVE-2026-90817) | Vanderbilt University Research Electronic Data Capture (REDCap) | Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability | 2026-11-21 |
| [CVE-2026-90436](https://nvd.nist.gov/vuln/detail/CVE-2026-90436) | Apache Axis | Apache Axis Unsafe Reflection Vulnerability | 2026-11-21 |
| [CVE-2026-115731](https://nvd.nist.gov/vuln/detail/CVE-2026-115731) | Perforce Puppet Enterprise | Perforce Puppet Enterprise Deserialization of Untrusted Data Vulnerability | 2026-12-01 |

---

*How this briefing is made: an automated pipeline pulls the last 30 hours of public feeds (CISA Advisories, BleepingComputer, The Hacker News, Krebs on Security, SecurityWeek, and the CISA KEV catalog). Gemini summarizes only what those articles' feed summaries say, and every story links to its original source. Read the source before acting on it.*
