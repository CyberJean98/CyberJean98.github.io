---
layout: post
title: "Daily Threat Briefing: FBI Database Hack, Microsoft Entra Exploitation, and Ghostscript RCE"
date: 2026-11-22
categories: [threat-intel]
sources: [BleepingComputer, CISA KEV, SecurityWeek, The Hacker News]
---

Today's briefing highlights a significant government database hack, a critical vulnerability exploited in Microsoft's Entra Connect Health, and a remote code execution flaw in Ghostscript.

### FBI Investigating Apparent Hack of Its Key National Criminal Justice Database

The FBI is investigating an apparent hack of a national law enforcement database that it maintains.

**Why it matters:** A potential breach of a critical national criminal justice database maintained by the FBI represents a severe national security and law enforcement threat.

**What to do:**

- Monitor official advisories from government agencies
- Review access controls for sensitive systems

*Source: [FBI Investigating Apparent Hack of Its Key National Criminal Justice Database, AP Source Says](https://www.securityweek.com/fbi-investigating-apparent-hack-of-its-key-national-criminal-justice-database-ap-source-says/), SecurityWeek, Nov 21, 2026*

### Microsoft Entra Connect Health Flaw Exploited to Steal Tenant Data

Microsoft is warning organizations that it suffered a data breach after attackers exploited a vulnerability in its Entra Connect Health service to gain unauthorized access to administrator email addresses and tenant configuration information.

**Why it matters:** Exploitation of a core Microsoft service like Entra Connect Health can lead to significant compromise of organizational identities and configurations.

**What to do:**

- Review Entra Connect Health logs for suspicious activity
- Rotate administrator credentials
- Apply all available patches for Microsoft services

*Source: [Microsoft Entra Connect Health flaw exploited to steal tenant data](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/), BleepingComputer, Nov 21, 2026*

### Researchers Demonstrate Ghostscript Sandbox-Escape RCE via Crafted File Uploads

A now-patched flaw in Ghostscript allows a crafted file to escape the program's security sandbox and run commands on the server that processes it. Ghostscript is the interpreter that many Linux servers use to convert uploaded PDFs, PostScript files, and images into other formats.

**Why it matters:** This vulnerability allows remote code execution on servers processing common file types, posing a significant risk to applications that handle user uploads.

**What to do:**

- Patch Ghostscript installations immediately
- Review file upload handling mechanisms and sanitize inputs

*Source: [Researchers Demonstrate Ghostscript Sandbox-Escape RCE via Crafted File Uploads in Popular Apps](https://thehackernews.com/2026/11/researchers-demonstrate-ghostscript.html), The Hacker News, Nov 22, 2026*

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
