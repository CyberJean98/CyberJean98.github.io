"""Seed the public sandbox with a realistic mix of security and general IT
helpdesk tickets, each with a hint visitors can reveal if they get stuck.

Run once after deploying: python -m scripts.seed_demo
Safe to re-run — it skips seeding if demo tickets already exist.
"""
from app.database import SessionLocal, engine, Base
from app import models

Base.metadata.create_all(bind=engine)

SAMPLE_TICKETS = [
    # --- Security / SOC ---
    {
        "category": "security",
        "title": "Multiple failed SSH logins from external IP",
        "description": "Ten failed login attempts against a public-facing host within two minutes, all targeting the root account.",
        "severity": models.Severity.high,
        "status": models.Status.open,
        "hint": "Check the source IP against a threat intel lookup (AbuseIPDB, GreyNoise). If it's a known scanner, block at the firewall and confirm root login is disabled entirely — it shouldn't be reachable over SSH in the first place.",
    },
    {
        "category": "security",
        "title": "Phishing email reported by finance team",
        "description": "Employee forwarded a suspicious invoice email requesting a wire transfer. Sender domain looks spoofed.",
        "severity": models.Severity.high,
        "status": models.Status.open,
        "hint": "Check the sender's actual return-path and SPF/DKIM results, not just the display name. Confirm whether anyone clicked or replied, and if so, treat it as a potential compromise — reset credentials and check mail forwarding rules.",
    },
    {
        "category": "security",
        "title": "Unpatched CVE flagged on dev server",
        "description": "Vulnerability scan flagged an outdated package version with a known remote code execution CVE.",
        "severity": models.Severity.critical,
        "status": models.Status.open,
        "hint": "Check whether the vulnerable service is actually exposed to the network (internet-facing vs internal-only) — that changes urgency. Patch or upgrade the package, and note the CVE ID and remediation date for compliance tracking.",
    },
    {
        "category": "security",
        "title": "Unusual after-hours file access",
        "description": "A service account accessed a shared drive at 3am local time, outside its normal automation schedule.",
        "severity": models.Severity.low,
        "status": models.Status.resolved,
        "hint": "Cross-reference against the scheduled job list — a lot of 'unusual' after-hours activity turns out to be a delayed backup or batch job. If nothing scheduled matches, check whether the account's credentials appear in any recent breach dumps.",
    },
    {
        "category": "security",
        "title": "Antivirus quarantined a file on an employee laptop",
        "description": "Endpoint protection flagged and quarantined a file downloaded from an email attachment. User says they were expecting the file from a coworker.",
        "severity": models.Severity.medium,
        "status": models.Status.open,
        "hint": "Get the file hash and check it against VirusTotal before assuming false positive. Verify with the coworker directly (not by replying to the email) that they actually sent it — attachment spoofing from a compromised contact is common.",
    },
    {
        "category": "security",
        "title": "Departing employee still has active VPN access",
        "description": "HR confirms an employee's last day was Friday. IT ticket to offboard access wasn't filed until the following Wednesday.",
        "severity": models.Severity.medium,
        "status": models.Status.in_progress,
        "hint": "Revoke VPN, SSO, and any local admin credentials immediately — the ticket delay is a process gap worth flagging separately. Check login logs for any access between their last day and the revocation.",
    },
    # --- General IT helpdesk ---
    {
        "category": "helpdesk",
        "title": "User locked out of account after password expiry",
        "description": "Employee changed their password remotely but their laptop still has the old one cached, causing repeated lockouts.",
        "severity": models.Severity.low,
        "status": models.Status.open,
        "hint": "Have them update the cached credential in Windows Credential Manager (or the macOS Keychain) manually — a remote password change doesn't always sync to a machine that was offline at the time.",
    },
    {
        "category": "helpdesk",
        "title": "Can't connect to company VPN from home",
        "description": "User gets a timeout error connecting to VPN from their home network. Works fine from the office.",
        "severity": models.Severity.medium,
        "status": models.Status.open,
        "hint": "Check whether their home router blocks the VPN protocol/port (common with some ISP routers and ports like UDP 500/4500 for IPsec). Try a different network (phone hotspot) to isolate whether it's the VPN client, the ISP, or the user's router.",
    },
    {
        "category": "helpdesk",
        "title": "Printer on 3rd floor not accepting jobs",
        "description": "Multiple users report print jobs stuck in queue since this morning. Printer shows as 'online' in the admin panel.",
        "severity": models.Severity.low,
        "status": models.Status.open,
        "hint": "Clear the print spooler queue and restart the print spooler service before touching the printer itself — a stuck job at the front of the queue often blocks everything behind it.",
    },
    {
        "category": "helpdesk",
        "title": "New hire laptop not receiving MDM policies",
        "description": "New employee's laptop was enrolled in the MDM system but isn't getting the expected software pushes or security policies.",
        "severity": models.Severity.medium,
        "status": models.Status.in_progress,
        "hint": "Confirm the device actually checked in after enrollment (some MDM agents need a manual sync or a reboot to pull policy). Also verify the device landed in the correct MDM group — misassigned groups are a common cause of missing pushes.",
    },
    {
        "category": "helpdesk",
        "title": "Shared calendar invites not syncing to mobile app",
        "description": "Team lead created a recurring meeting on the shared calendar. Some team members see it on desktop but not on their phones.",
        "severity": models.Severity.low,
        "status": models.Status.open,
        "hint": "Check whether the affected users have the shared calendar actually subscribed/checked in their mobile app's calendar list — desktop and mobile clients sometimes maintain separate subscription settings.",
    },
    {
        "category": "helpdesk",
        "title": "Software license seats maxed out",
        "description": "Design team can't open the shared design tool. Admin panel shows all licensed seats are in use, but several are assigned to former employees.",
        "severity": models.Severity.medium,
        "status": models.Status.open,
        "hint": "Reclaim seats from departed employees' accounts first — this is usually faster and cheaper than buying more licenses, and it's worth checking whether offboarding should include license deprovisioning going forward.",
    },
    {
        "category": "helpdesk",
        "title": "Slow laptop performance reported by sales rep",
        "description": "User says their laptop has become noticeably slower over the past week, especially when opening the CRM.",
        "severity": models.Severity.low,
        "status": models.Status.closed,
        "hint": "Check startup programs and background processes first — a surprising number of 'slow laptop' tickets trace back to an update or agent that started running at boot. Also check disk space; a nearly-full drive slows everything down.",
    },
]


def seed():
    db = SessionLocal()
    try:
        existing = db.query(models.Ticket).filter(models.Ticket.is_demo.is_(True)).count()
        if existing > 0:
            print(f"Sandbox already has {existing} demo ticket(s) — skipping seed.")
            return

        for t in SAMPLE_TICKETS:
            ticket = models.Ticket(
                title=t["title"],
                description=t["description"],
                severity=t["severity"],
                status=t["status"],
                source=models.Source.manual,
                is_demo=True,
                category=t["category"],
                hint=t["hint"],
            )
            db.add(ticket)
        db.commit()
        print(f"Seeded {len(SAMPLE_TICKETS)} demo tickets into the sandbox.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
