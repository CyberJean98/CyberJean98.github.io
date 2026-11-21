---
layout: post
title: "Daily Threat Intel: CISA Alerts, Zero-Days, and Major Service Exploits"
date: 2026-11-21
categories: [threat-intel]
sources: [BleepingComputer, CISA KEV, SecurityWeek, The Hacker News]
---

Today's briefing highlights critical vulnerabilities actively exploited, a zero-day discovered by AI agents, and a significant breach impacting a major cloud service.

### Hackers Exploit Critical VMware, Cisco, and Apache Flaws as Espionage Attacks Emerge

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added four flaws impacting Apache Roller, Cisco Expressway, SAP NetWeaver, and Broadcom VMware vCenter to its Known Exploited Vulnerabilities (KEV) list. This action cites evidence of active exploitation of these vulnerabilities, which are being used in emerging espionage attacks.

**Why it matters:** CISA's addition of these vulnerabilities to its KEV catalog indicates they pose significant risk due to confirmed active exploitation. Organizations using these products must prioritize patching to defend against potential espionage campaigns.

**What to do:**

- Patch affected systems immediately
- Monitor for indicators of compromise

*Source: [Hackers Exploit Critical VMware, Cisco, and Apache Flaws as Espionage Attacks Emerge](https://thehackernews.com/2026/11/hackers-exploit-critical-vmware-cisco.html), The Hacker News, Nov 21, 2026*

### Amazon: China-Linked Hackers’ AI Agents Exploited Medical Software Zero-Day

Amazon reported that a threat actor used autonomous Cairn AI agents to discover and exploit a critical MONAI Label vulnerability. This exploitation involved a zero-day flaw in medical software.

**Why it matters:** This incident demonstrates the evolving capabilities of threat actors, leveraging AI agents to find and exploit previously unknown vulnerabilities. Organizations using medical software should be aware of this advanced exploitation technique.

**What to do:**

- Review medical software for vulnerabilities
- Implement robust monitoring for unusual activity

*Source: [Amazon: China-Linked Hackers’ AI Agents Exploited Medical Software Zero-Day](https://www.securityweek.com/amazon-china-linked-hackers-ai-agents-exploited-medical-software-zero-day/), SecurityWeek, Nov 21, 2026*

### Microsoft Entra Connect Health flaw exploited to access tenant data

Microsoft has warned organizations about a data breach stemming from attackers exploiting a vulnerability in its Entra Connect Health service. This exploitation led to unauthorized access to administrator email addresses and tenant configuration information.

**Why it matters:** The exploitation of a flaw in a critical identity and access management service like Microsoft Entra Connect Health can have widespread implications. Unauthorized access to administrative credentials and configuration data poses a severe risk to organizational security.

**What to do:**

- Review Microsoft Entra Connect Health logs for suspicious activity
- Enforce strong authentication for administrative accounts
- Rotate credentials if compromised

*Source: [Microsoft Entra Connect Health flaw exploited to access tenant data](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-access-tenant-data/), BleepingComputer, Nov 21, 2026*

### Newly added to CISA's Known Exploited Vulnerabilities catalog

These are confirmed to be exploited in the wild. Federal agencies must patch by the due date, and everyone else should treat them as urgent.

| CVE | Vendor / product | Vulnerability | Patch by |
| --- | --- | --- | --- |
| [CVE-2026-129448](https://nvd.nist.gov/vuln/detail/CVE-2026-129448) | Apache Roller | Apache Roller Deserialization of Untrusted Data Vulnerability | 2026-11-23 |
| [CVE-2026-123890](https://nvd.nist.gov/vuln/detail/CVE-2026-123890) | Broadcom VMware vCenter | VMWare vCenter Authentication Bypass Using an Alternate Path or Channel Vulnerability | 2026-11-23 |
| [CVE-2025-42884](https://nvd.nist.gov/vuln/detail/CVE-2025-42884) | SAP NetWeaver | SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability | 2026-11-23 |
| [CVE-2026-76466](https://nvd.nist.gov/vuln/detail/CVE-2026-76466) | Cisco Expressway Series | Cisco Expressway Series Use of Hard-coded Credentials Vulnerability | 2026-11-23 |

---

*How this briefing is made: an automated pipeline pulls the last 30 hours of public feeds (CISA Advisories, BleepingComputer, The Hacker News, Krebs on Security, SecurityWeek, and the CISA KEV catalog). Gemini summarizes only what those articles' feed summaries say, and every story links to its original source. Read the source before acting on it.*
