---
layout: post
title: "Daily Threat Briefing: Drupal RCE, FinCEN Breach, and VMware Critical Patches"
date: 2026-11-25
categories: [threat-intel]
sources: [BleepingComputer, CISA KEV, SecurityWeek, The Hacker News]
---

Today's briefing covers active exploitation of a critical Drupal flaw, a cyber intrusion impacting a U.S. Treasury agency, and urgent patches for VMware vulnerabilities.

### Hackers now exploit critical Drupal RCE flaw to hijack sites

The Drupal security team has confirmed that a critical vulnerability that lets attackers hijack unpatched sites has been actively exploited since at least Thursday. This flaw allows attackers to take full control of affected Drupal sites.

**Why it matters:** This critical remote code execution (RCE) flaw poses a severe risk to web infrastructure, as attackers can fully compromise unpatched Drupal sites.

**What to do:**

- Patch Drupal installations immediately
- Monitor web server logs for suspicious activity

*Source: [Hackers now exploit critical Drupal RCE flaw to hijack sites](https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-drupal-rce-flaw-to-hijack-sites/), BleepingComputer, Nov 25, 2026*

### U.S. Treasury's Financial Crimes Agency Takes Some Systems Offline After Cyber Intrusion

The U.S. Treasury Department's Financial Crimes Enforcement Network (FinCEN) has been hit by a cybersecurity incident that resulted in "unauthorized access to a limited subset of its systems." As a precaution, the bureau has taken some systems offline.

**Why it matters:** A cyber intrusion affecting a U.S. government financial agency highlights the persistent threat to critical government infrastructure and sensitive data.

**What to do:**

- Review access logs for unusual activity
- Implement robust access controls and multi-factor authentication
- Ensure incident response plans are up-to-date

*Source: [U.S. Treasury's Financial Crimes Agency Takes Some Systems Offline After Cyber Intrusion](https://thehackernews.com/2026/11/us-treasurys-fincen-takes-some-systems.html), The Hacker News, Nov 25, 2026*

### VMware Updates Patch Critical ESX, vCenter Vulnerabilities

VMware has released updates to patch critical vulnerabilities affecting ESX and vCenter. These critical bugs include an authentication bypass in vCenter and flaws that could allow code execution on ESX hosts.

**Why it matters:** Critical vulnerabilities in widely used virtualization platforms like VMware ESX and vCenter can lead to full system compromise, impacting numerous virtualized environments.

**What to do:**

- Apply VMware updates and patches immediately
- Verify authentication mechanisms are properly configured
- Review network segmentation for critical virtualization infrastructure

*Source: [VMware Updates Patch Critical ESX, vCenter Vulnerabilities](https://www.securityweek.com/vmware-updates-patch-critical-esx-vcenter-vulnerabilities/), SecurityWeek, Nov 24, 2026*

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
| [CVE-2026-133968](https://nvd.nist.gov/vuln/detail/CVE-2026-133968) | Project MONAI MONAI Label | Project MONAI MONAI Label Path Traversal Vulnerability | 2026-11-26 |
| [CVE-2026-134624](https://nvd.nist.gov/vuln/detail/CVE-2026-134624) | N-able MailAssure | N-able MailAssure (SpamExperts) Server-Side Request Forgery (SSRF) Vulnerability | 2026-11-26 |

---

*How this briefing is made: an automated pipeline pulls the last 30 hours of public feeds (CISA Advisories, BleepingComputer, The Hacker News, Krebs on Security, SecurityWeek, and the CISA KEV catalog). Gemini summarizes only what those articles' feed summaries say, and every story links to its original source. Read the source before acting on it.*
