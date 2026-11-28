---
layout: post
title: "Critical Zero-Day, Government Breach, and Password Manager Attack"
date: 2026-11-28
categories: [threat-intel]
sources: [BleepingComputer, CISA KEV, The Hacker News]
---

This briefing highlights a critical zero-day vulnerability, a significant government cloud platform breach, and a cyber attack on a popular password manager.

### Unpatched Cacti zero-day with public PoC gives remote code execution

A zero-day vulnerability in the Cacti network monitoring platform has been publicly disclosed. A proof-of-concept exploit is available, allowing unauthenticated attackers to execute commands on vulnerable servers.

**Why it matters:** This is a critical vulnerability in a network monitoring platform with a publicly available exploit. Unauthenticated remote code execution poses a severe risk to affected systems.

**What to do:**

- Patch Cacti installations immediately when a fix is released
- Monitor Cacti servers for unusual activity
- Restrict network access to Cacti instances

*Source: [Unpatched Cacti zero-day with public PoC gives remote code execution](https://www.bleepingcomputer.com/news/security/unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution/), BleepingComputer, Nov 27, 2026*

### US Air Force cloud platform reportedly hacked in latest federal breach

The US Air Force's Cloud One computing platform has reportedly been breached by hackers. This incident follows a recent series of cyberattacks affecting other US government agencies, including the FBI, CIA, and Treasury Department.

**Why it matters:** A breach of a US Air Force cloud platform is a significant event, indicating potential compromise of sensitive government data and systems. It highlights ongoing threats to federal infrastructure.

**What to do:**

- Review cloud security configurations
- Implement robust access controls and monitoring for cloud environments
- Ensure multi-factor authentication is enforced

*Source: [US Air Force cloud platform reportedly hacked in latest federal breach](https://www.bleepingcomputer.com/news/security/us-air-force-cloud-platform-reportedly-hacked-in-latest-federal-breach/), BleepingComputer, Nov 27, 2026*

### pCloud Password Manager Hit by Cyber Attack Involving Email Address Exposure and Login Attempts

Cross-platform password manager pCloud Pass confirmed it was targeted by a cyber attack after users reported unknown devices connecting to their accounts. The Swiss company stated the attack was promptly contained, but a small number of user email addresses were unfortunately exposed.

**Why it matters:** A cyber attack on a password manager is highly concerning as it could lead to credential compromise and subsequent access to other online accounts. The exposure of email addresses and suspicious login attempts indicate a direct threat to user security.

**What to do:**

- Users of pCloud Pass should change their master password immediately
- Enable multi-factor authentication on all critical accounts
- Monitor accounts for suspicious login attempts

*Source: [pCloud Password Manager Hit by Cyber Attack Involving Email Address Exposure and Login Attempts](https://thehackernews.com/2026/11/pcloud-password-manager-hit-by-cyber.html), The Hacker News, Nov 28, 2026*

### Newly added to CISA's Known Exploited Vulnerabilities catalog

These are confirmed to be exploited in the wild. Federal agencies must patch by the due date, and everyone else should treat them as urgent.

| CVE | Vendor / product | Vulnerability | Patch by |
| --- | --- | --- | --- |
| [CVE-2026-120705](https://nvd.nist.gov/vuln/detail/CVE-2026-120705) | OSGeo GeoServer | OSGeo GeoServer XML Injection Vulnerability | 2026-11-30 |
| [CVE-2026-129243](https://nvd.nist.gov/vuln/detail/CVE-2026-129243) | OSGeo GeoServer | OSGeo GeoServer Incorrect Authorization Vulnerability | 2026-11-30 |
| [CVE-2026-136716](https://nvd.nist.gov/vuln/detail/CVE-2026-136716) | Drupal Core | Drupal Core Improper Check for Unusual or Exceptional Conditions Vulnerability | 2026-11-30 |

---

*How this briefing is made: an automated pipeline pulls the last 30 hours of public feeds (CISA Advisories, BleepingComputer, The Hacker News, Krebs on Security, SecurityWeek, and the CISA KEV catalog). Gemini summarizes only what those articles' feed summaries say, and every story links to its original source. Read the source before acting on it.*
