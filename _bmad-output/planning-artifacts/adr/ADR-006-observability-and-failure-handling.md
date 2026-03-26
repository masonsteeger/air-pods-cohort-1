# ADR-006: Observability and Failure Handling

**Status:** Accepted
**Date:** 2026-03-26

## Decision

Two complementary alerting mechanisms. Dawn is never notified.

| Mechanism | Purpose | Tool |
|---|---|---|
| Slack webhook | Active failure alerts (pipeline errors) | Incoming webhook to technical team channel |
| Dead man's switch | Silent failure detection (pipeline stops running) | Healthchecks.io |

## Dead Man's Switch Behavior

- Healthchecks.io expects a ping every 12 hours (+ grace period)
- Ping is sent only on full pipeline success
- If no ping is received within the window, Healthchecks.io fires an alert
- Catches failures the active error handler cannot: misconfigured cron, exhausted Azure quota, infrastructure outage

## Diagnostic Access

- Raw fetched data is written to Azure Blob Storage with a timestamp before any transformation
- IT can retrieve the exact payload the pipeline received from Google Sheets for any run
- Allows distinguishing between "bad data in the sheet" vs. "pipeline logic error" without Dawn's involvement

## Dawn's Burden on Failure

Zero. The technical team owns detection, diagnosis, and recovery entirely.
