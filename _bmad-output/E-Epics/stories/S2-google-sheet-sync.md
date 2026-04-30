# S2: Google Sheet Sync Pipeline

**Epic:** 01 — Public Event Calendar MVP
**Priority:** P1
**Estimate:** L
**Status:** Ready

---

## User Story

**As a** system
**I want** to sync events from Dawn's Google Sheet
**So that** the `/events` endpoint reflects current data without manual intervention

---

## Acceptance Criteria

- [ ] Reads from existing Google Sheet (no new Dawn workflow)
- [ ] Best-effort sync frequency (at least daily)
- [ ] Generates JSON matching S1 schema
- [ ] Handles missing/malformed rows gracefully (skip, don't crash)
- [ ] Zero maintenance burden on Dawn
- [ ] Logs sync timestamp for freshness indicator

---

## Technical Notes

### Input: Google Sheet

Dawn's existing sheet contains event data. Required columns:
- Group name
- Event title
- Start date/time
- Status (active/cancelled)
- Meetup URL

### Output: JSON File

Generated `events.json` (or equivalent) consumed by `/events` endpoint.

### Sync Options

1. **GitHub Action** — Scheduled workflow reads sheet, commits JSON
2. **Serverless function** — Triggered on schedule, writes to storage
3. **Build-time** — Static site generator fetches at build

### Authentication

- Google Sheets API with service account (read-only)
- Sheet must be shared with service account email

---

## Edge Cases

| Scenario | Handling |
|----------|----------|
| Row missing required field | Skip row, log warning |
| Invalid date format | Skip row, log warning |
| Sheet unavailable | Keep previous JSON, log error |
| Empty sheet | Generate empty array `[]` |

---

## References

- `planning-artifacts/architecture.md`
- `planning-artifacts/adr/ADR-002-google-sheets-range-strategy.md`
