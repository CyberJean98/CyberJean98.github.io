# SOC Ticketing Console

A lightweight incident ticketing system built for cybersecurity portfolio
work, living inside this site's repo. It's a working, visitable app — not a
demo screenshot — where real tickets can be filed manually or created
automatically from Wazuh SIEM alerts.

**Live at:** `cyberjean98.github.io/ticketing/` _(update once deployed)_

## Why this project

Most SOC analyst, help desk, and IT support roles list a ticketing platform
(Jira, ServiceNow, Zendesk, etc.) as required experience. This project builds
one from the ground up so I can speak fluently about the full lifecycle:
alert → ticket → triage → assignment → resolution → audit trail — not just
use someone else's tool.

## Repo layout

This lives alongside the Jekyll blog in the same repo, split so GitHub Pages
only ever touches the static frontend:

```
CyberJean98.github.io/
├── (existing Jekyll blog files — untouched)
├── ticketing/
│   └── index.html          ← static frontend, served by GitHub Pages
│                              at cyberjean98.github.io/ticketing/
├── ticketing-backend/
│   ├── app/                ← FastAPI backend
│   ├── scripts/seed_demo.py
│   └── requirements.txt
└── render.yaml             ← tells Render to build from ticketing-backend/
```

Jekyll only processes Markdown/Liquid — `ticketing/index.html` has no Liquid
syntax, so Jekyll copies it through untouched. The Python backend never gets
near GitHub Pages at all; Render reads `render.yaml`'s `rootDir` and builds
only from `ticketing-backend/`.

## Architecture

```
Wazuh (home lab SIEM)  ──alert──▶  FastAPI backend   ◀──REST──  ticketing/index.html
                                    (Render)                     (GitHub Pages)
                                    │
                                    ▼
                              PostgreSQL (Render)
```

- **Backend**: FastAPI (Python), SQLAlchemy ORM, JWT auth — deployed on Render
- **Database**: SQLite for local dev, PostgreSQL in production (Render)
- **Frontend**: single-page HTML/CSS/vanilla JS, no build step, served
  directly by GitHub Pages as part of this site
- **Wazuh integration**: a webhook endpoint (`/webhooks/wazuh/alert`) that
  auto-creates a ticket when an alert crosses a configurable severity
  threshold, with severity mapped from the Wazuh rule level

## Features

- Ticket CRUD with severity (low/medium/high/critical) and status
  (open/in-progress/resolved/closed)
- Category tagging (security / helpdesk / visitor-submitted) with filtering
- JWT-based login/registration
- Notes/comment thread per ticket
- Full audit log on every status change, severity change, and assignment
- Wazuh webhook ingestion with a shared-secret header and a configurable
  "ignore below this level" threshold, so noisy low-level alerts don't flood
  the board
- Filtering by status, severity, and category

## It's a practice tool, not just a demo

The sandbox is seeded with a realistic mix of security and general IT
helpdesk tickets (phishing reports, VPN issues, license problems, suspicious
logins, printer chaos, offboarding gaps, and more) — see
`ticketing-backend/scripts/seed_demo.py` for the full set.

- **Visitors can submit real problems.** The "file a ticket" form is framed
  as an invitation to bring an actual workplace issue, not just click a demo
  button.
- **Every ticket can carry a hint.** Visitors get a "Show hint" button on any
  ticket; only the admin account can write or edit a hint (via the same
  detail panel). That means seeded practice tickets ship with built-in
  troubleshooting guidance, and you can add a hint to a visitor's real
  submission after the fact — effectively answering their question in place.

## Access model: admin vs. public sandbox

Since this app is meant to be genuinely usable by site visitors, not just
viewed, it splits access into two tiers so real lab data never gets exposed:

- **Admin (you)**: the *first account ever registered* automatically becomes
  admin. Admin sees and manages everything — including real Wazuh alerts from
  your lab and any ticket you create yourself.
- **Visitors**: everyone who registers after that gets a `visitor` role.
  Visitors only ever see and interact with sandbox tickets (`is_demo=True`) —
  seeded sample data, plus anything they create themselves. They cannot see,
  list, or access real tickets even by guessing an ID (returns a plain 404).

Real Wazuh alerts are always created with `is_demo=False`, so they're
admin-only by construction.

**Important**: register your own admin account immediately after first
deploying, before linking `/ticketing/` anywhere public — the first
registration wins.

Run `python -m scripts.seed_demo` (from inside `ticketing-backend/`) once
after deploying, to populate the public sandbox with sample tickets so
visitors don't land on an empty board.

## Local development

```bash
cd ticketing-backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

uvicorn app.main:app --reload
```

The API comes up at `http://127.0.0.1:8000`, with interactive docs at
`http://127.0.0.1:8000/docs`.

To use the frontend locally, open `ticketing/index.html` in a browser. It
points at `http://127.0.0.1:8000` by default — set `window.API_BASE` at the
top of the `<script>` block if your backend runs elsewhere.

## Deploying the backend (Render, free tier)

The `render.yaml` Blueprint at the repo root provisions both the web service
and a free PostgreSQL database, building only from `ticketing-backend/`:

1. Push this repo (with your existing blog content plus these two new
   folders and `render.yaml`) to GitHub.
2. In Render, choose **New > Blueprint** and point it at the repo.
3. Render reads `render.yaml`, builds from `ticketing-backend/`, and
   auto-generates `SECRET_KEY` and `WAZUH_WEBHOOK_SECRET`.
4. Once deployed, note the service URL (e.g.
   `https://soc-ticketing-api.onrender.com`).

Note: on Render's free tier, the service sleeps after inactivity and takes
~30-60 seconds to wake up on the next request — expected behavior, not a bug,
worth mentioning to visitors or interviewers.

## Publishing the frontend

Before your next push, set `window.API_BASE` near the top of the `<script>`
block in `ticketing/index.html` to your live Render URL. GitHub Pages will
pick up the change automatically on the next deploy of this repo, and the
page will be live at `cyberjean98.github.io/ticketing/`.

## Wiring up real Wazuh alerts

On your Wazuh manager, add an integration (or use `ossec.conf` active
response / a small script) that POSTs to:

```
POST https://<your-render-url>/webhooks/wazuh/alert
Header: X-Webhook-Secret: <the value Render generated>
Body:
{
  "rule_id": "<wazuh rule id>",
  "rule_description": "<wazuh rule description>",
  "rule_level": <int>,
  "agent_name": "<agent hostname>",
  "full_log": "<raw log line>"
}
```

Adjust `WAZUH_MIN_RULE_LEVEL` (env var, default `7`) to control how much
gets escalated to a ticket versus ignored as noise.

## What's next

- Ticket assignment to specific users with a "my tickets" view
- SLA/aging timers and a basic reporting dashboard (tickets by severity,
  mean time to resolve)
- Link to `/ticketing/` from the blog's nav so visitors can find it
