---
layout: post
title: "Threat Intel Briefing: Zero-Days Exploited, Major Breaches, and Critical Patches"
date: 2026-11-20
categories: [threat-intel]
sources: [BleepingComputer, CISA KEV, The Hacker News]
---

This briefing highlights recent active exploitation of critical vulnerabilities, significant data breaches, and urgent security updates for key enterprise systems.

### China-Linked Hackers Exploit Critical VMware vCenter Zero-Day to Gain Admin Access and Steal Data

The suspected China-nexus cyber espionage group known as Armory Castle has been attributed to the zero-day exploitation of a critical security flaw in VMware vCenter Server. This vulnerability is an authentication bypass in the VMware Directory Service that could be exploited to gain unauthorized access, allowing attackers to gain admin access and steal data.

**Why it matters:** This is an actively exploited zero-day in a critical enterprise management tool, allowing sophisticated attackers to gain administrative access and steal sensitive data.

**What to do:**

- Patch VMware vCenter Server immediately
- Monitor for signs of compromise and unauthorized access

*Source: [China-Linked Hackers Exploit Critical VMware vCenter Zero-Day to Gain Admin Access and Steal Data](https://thehackernews.com/2026/11/china-linked-hackers-exploit-critical.html), The Hacker News, Nov 20, 2026*

### Bell Canada says 'agentic' hacker stole enterprise customer data

Bell Canada has confirmed that an "agentic" threat actor breached its systems. The incident resulted in the theft of enterprise customer data, including information from a system used to order and provision telecommunications circuits.

**Why it matters:** A major telecommunications provider suffered a breach, leading to the theft of sensitive enterprise customer data.

**What to do:**

- Review third-party access and security protocols
- Enhance monitoring for unusual data access and exfiltration

*Source: [Bell Canada says 'agentic' hacker stole enterprise customer data](https://www.bleepingcomputer.com/news/security/bell-canada-says-agentic-hacker-stole-enterprise-customer-data/), BleepingComputer, Nov 20, 2026*

### F5 releases emergency patches for critical BIG-IP RCE flaws

US cybersecurity company F5 warned customers to patch five critical BIG-IP vulnerabilities. Attackers can exploit these flaws to trigger denial-of-service (DoS) or gain remote code execution.

**Why it matters:** Critical vulnerabilities in F5 BIG-IP could allow remote code execution or denial-of-service, impacting essential network infrastructure and requiring immediate attention.

**What to do:**

- Apply F5's emergency patches immediately to all affected BIG-IP systems
- Verify patch installation and system integrity

*Source: [F5 releases emergency patches for critical BIG-IP RCE flaws](https://www.bleepingcomputer.com/news/security/f5-releases-emergency-patches-for-critical-big-ip-rce-flaws/), BleepingComputer, Nov 20, 2026*

### Newly added to CISA's Known Exploited Vulnerabilities catalog

These are confirmed to be exploited in the wild. Federal agencies must patch by the due date, and everyone else should treat them as urgent.

| CVE | Vendor / product | Vulnerability | Patch by |
| --- | --- | --- | --- |
| [CVE-2026-129448](https://nvd.nist.gov/vuln/detail/CVE-2026-129448) | Apache Roller | Apache Roller Deserialization of Untrusted Data Vulnerability | 2026-11-23 |
| [CVE-2026-123890](https://nvd.nist.gov/vuln/detail/CVE-2026-123890) | Broadcom VMware vCenter | VMWare vCenter Authentication Bypass Using an Alternate Path or Channel Vulnerability | 2026-11-23 |
| [CVE-2025-42884](https://nvd.nist.gov/vuln/detail/CVE-2025-42884) | SAP NetWeaver | SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability | 2026-11-23 |
| [CVE-2026-76466](https://nvd.nist.gov/vuln/detail/CVE-2026-76466) | Cisco Expressway Series | Cisco Expressway Series Use of Hard-coded Credentials Vulnerability | 2026-11-23 |
| [CVE-2024-10441](https://nvd.nist.gov/vuln/detail/CVE-2024-10441) | Synology DiskStation Manager (DSM) | Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability | 2026-11-21 |
| [CVE-2026-40217](https://nvd.nist.gov/vuln/detail/CVE-2026-40217) | BerriAI LiteLLM | BerriAI LiteLLM Unprotected Alternate Channel Vulnerability | 2026-12-02 |
| [CVE-2026-90817](https://nvd.nist.gov/vuln/detail/CVE-2026-90817) | Vanderbilt University Research Electronic Data Capture (REDCap) | Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability | 2026-11-21 |
| [CVE-2026-90436](https://nvd.nist.gov/vuln/detail/CVE-2026-90436) | Apache Axis | Apache Axis Unsafe Reflection Vulnerability | 2026-11-21 |

---

*How this briefing is made: an automated pipeline pulls the last 30 hours of public feeds (CISA Advisories, BleepingComputer, The Hacker News, Krebs on Security, SecurityWeek, and the CISA KEV catalog). Gemini summarizes only what those articles' feed summaries say, and every story links to its original source. Read the source before acting on it.*
