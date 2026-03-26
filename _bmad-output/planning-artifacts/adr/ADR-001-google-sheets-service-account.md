# ADR-001: Google Sheets Access via Service Account

**Status:** Accepted
**Date:** 2026-03-26

## Decision

Use Google Sheets API v4 with a dedicated service account for all sheet reads.

## Rejected Alternative

Google Sheets "Publish to Web" as CSV.

## Rationale

- Published CSV now requires the underlying sheet to be set to "Anyone with the link can view," exposing all of Dawn's data publicly — an unacceptable privacy risk
- Published CSV has documented, ongoing reliability issues (broken downloads, stale cache, format changes)
- Service account keeps Dawn's sheet private; only the service account email is granted read-only access (one-time share, performed by IT — not Dawn)
- Service account credentials are stored in Azure Key Vault, not in the repository

## Implementation Notes

- One-time setup: IT shares Dawn's sheet with the service account email (read-only)
- Dawn performs no new actions — she edits her sheet exactly as before
