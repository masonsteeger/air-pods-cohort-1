# ADR-003: Pipeline Architecture — Scheduled Azure Function

**Status:** Accepted
**Date:** 2026-03-26

## Decision

Implement the data pipeline as an Azure Function with a Timer Trigger running every 12 hours.

## Pipeline Flow

```
Timer fires (every 12 hours)
      ↓
[Fetch] Google Sheets API via service account
        Credentials retrieved from Azure Key Vault
        Range: Sheet1!A:G (open-ended, header-mapped)
      ↓
[Store] Raw fetched data → Azure Blob Storage
        Path: diagnostics/{timestamp}/raw-fetch.json
        Retained for IT diagnostic access
      ↓
[Transform] Parse and normalize to events schema (TBD)
      ↓
[Publish] events.json → Azure Blob Storage (public endpoint)
        Previous version remains live until publish succeeds
        No overwrite on failure
      ↓
[Heartbeat] HTTP ping to Healthchecks.io (dead man's switch)
        Ping fires ONLY after full successful completion
      ↓
[On any failure] POST to Slack webhook → technical team channel
```

## Rationale

- Azure Functions Timer Trigger is consistent with Improving's existing Azure infrastructure — no new vendor
- 12-hour cadence is well within the 24-hour sync tolerance
- Pipeline is stateless — each run fetches from source and publishes fresh; no database required
- Failed runs do not overwrite the live `events.json` — the previous successful build stays live
