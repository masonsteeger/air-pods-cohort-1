# ADR-002: Google Sheets Range Strategy

**Status:** Accepted
**Date:** 2026-03-26

## Decision

Read an open-ended column range (`Sheet1!A:G`) using header-name mapping, not positional column mapping.

## Rationale

- Open-ended range (`A:G`) automatically includes new rows as Dawn adds groups — no configuration change required
- Header-name mapping (locate the row where `"Event Name"` appears, map all subsequent rows by header) is resilient to column reordering and insertion
- Positional mapping (column C = date) breaks silently if Dawn inserts a column — header mapping surfaces that as an explicit, detectable error

## Contract

The pipeline depends on specific header names in row 1 of the sheet. These header names are the agreed interface between Dawn's sheet and the pipeline. Changes to header names require a coordinated update.

## Privacy

The pipeline reads only the configured column range. Columns Dawn adds outside that range are never accessed.
