# Design Log

Project: air-pods-cohort-1
Output Folder: _bmad-output

---

## Current

- **Phase 3: UX Scenarios (Freya) — in progress.** Steps 1–6 of 9 complete. Four scenarios outlined and saved; overview index generated. Paused for session break on 2026-04-23. Resume at **step 7 (Quality Review)** → step 8 (Design Log completion) → step 9 (Phase 4 Handover).

## Backlog

- Phase 3 step 7: Quality review against rubric
- Phase 3 step 8: Update design log with Phase 3 completion entry
- Phase 3 step 9: Handover to Phase 4 (UX Design)
- Phase 4: UX Design (Freya) — to start after Phase 3 handover; must begin with reconciliation against existing out-of-band artifacts in `planning-artifacts/` and `implementation-artifacts/`

## Progress

### 2026-04-16 - Phase 1: Product Brief Complete

**Agent:** Saga (Product Brief)
**Brief Level:** Complete

**Artifacts Created:**
- `A-Product-Brief/project-brief.md`

**Summary:** Product strategy is documented for a public, sheet-powered event calendar for Improving-hosted groups. Core constraints and boundaries are explicit, including zero additional burden on Dawn and stable URL discoverability. Success criteria, positioning, and release priorities are captured as Phase 1 foundation.

**Next:** Phase 2 - Trigger Mapping

### 2026-04-16 - Phase 2: Trigger Mapping Complete

**Agent:** Saga (Trigger Mapping)
**Personas:** 5 (Prospective Pete, Imani the Improver, Dawn the Dynamo, Oscar the Organizer, Harold the Host)
**Business Goals:** 3

**Artifacts Created:**
- `B-Trigger-Map/01-Business-Goals.md`
- `B-Trigger-Map/02-Target-Groups.md`
- `B-Trigger-Map/03-Feature-Impact-Analysis.md`
- `B-Trigger-Map/trigger-map.md`
- `B-Trigger-Map/personas/04-prospective-pete.md`
- `B-Trigger-Map/personas/05-imani-the-improver.md`
- `B-Trigger-Map/personas/06-dawn-the-dynamo.md`
- `B-Trigger-Map/personas/07-oscar-the-organizer.md`
- `B-Trigger-Map/personas/08-harold-the-host.md`

**Summary:** Trigger Mapping defines prioritized business goals, personas, driving forces, and feature impact rankings tied to user psychology. The strategy emphasizes unified event discovery and operational sustainability, with Dawn's zero-burden constraint treated as non-negotiable. Output is sufficient to hand off into Phase 3 UX Scenarios.

**Next:** Phase 3 - UX Scenarios

### 2026-04-23 - Phase 3: UX Scenarios IN PROGRESS (paused mid-workflow)

**Agent:** Freya (UX Designer)
**Workflow:** `_bmad/wds/workflows/3-scenarios/`
**Mode:** Suggest mode (Freya drafts, Improver approves)

**Steps completed (1–6 of 9):**
1. ✅ Load context — Product Brief, Trigger Map, 5 personas loaded
2. ✅ Analyze scope — Presentation site, 2 pages, Small scale, Dream mode
3. ✅ Build strategic context — 4 scenario chains (Harold dropped; Dawn not a UX persona)
4. ✅ Suggest scenarios — plan approved
5. ✅ Outline scenarios — all 4 written and saved
6. ✅ Generate overview — `00-ux-scenarios.md` index created

**Steps remaining (7–9):**
7. ⏳ Quality review against WDS rubric (`data/quality-checklist.md`, `data/validation-standards.md`)
8. ⏳ Update design log with formal Phase 3 completion entry
9. ⏳ Handover to Phase 4

**Artifacts Created:**
- `C-UX-Scenarios/00-ux-scenarios.md` (master index)
- `C-UX-Scenarios/01-petes-unified-discovery/01-petes-unified-discovery.md`
- `C-UX-Scenarios/01-petes-unified-discovery/1.1-calendar-home/1.1-calendar-home.md` (canonical page spec for Calendar Home)
- `C-UX-Scenarios/02-imanis-weekly-check-in/02-imanis-weekly-check-in.md`
- `C-UX-Scenarios/02-imanis-weekly-check-in/2.1-calendar-home/2.1-calendar-home.md` (Imani's context + added requirements on shared canvas)
- `C-UX-Scenarios/03-oscars-share-moment/03-oscars-share-moment.md`
- `C-UX-Scenarios/03-oscars-share-moment/3.1-calendar-home/3.1-calendar-home.md` (Oscar's context + added requirements on shared canvas)
- `C-UX-Scenarios/04-petes-stale-link-rebound/04-petes-stale-link-rebound.md`
- `C-UX-Scenarios/04-petes-stale-link-rebound/4.1-not-found/4.1-not-found.md`

**Resume instructions for next session:**
1. Re-invoke Freya (`/freya` or equivalent) — she will detect this in-progress state from the Current table and pick up at step 7.
2. Step 7 runs quality review against `_bmad/wds/workflows/3-scenarios/data/quality-checklist.md` and `validation-standards.md`.
3. After step 9, Freya hands off to Phase 4 which should begin with reconciliation against `planning-artifacts/ux-design-specification.md`, `calendar-layout-options.md`, and `implementation-artifacts/spec-quick-prototype-*`.

**Cross-scenario design tensions flagged for Phase 4 (captured in `00-ux-scenarios.md`):**
- Row information hierarchy on Calendar Home (Pete wants group+topic, Imani wants location, Oscar wants group)
- Identity anchor prominence (Oscar's scenario requires visible "Improving Community Calendar" branding on both Calendar Home and 404)
- Mixed scenario endpoints — scenarios 01 (external) and 02/03 (internal) end differently; page must be gateway AND standalone destination

## Key Decisions

| Date | Decision | Context | Participants |
|------|----------|---------|-------------|
| 2026-04-16 | Public calendar remains projection of existing Google Sheet (no new Dawn workflows) | Phase 1: Product Brief | Saga + Improver |
| 2026-04-16 | MVP prioritizes unified listing, stable URL, auto-sync, and Meetup click-through | Phase 2: Trigger Mapping | Saga + Improver |
| 2026-04-16 | Saga artifacts normalized into `_bmad-output` canonical paths | Process normalization | Cascade + Improver |
| 2026-04-23 | Treat existing UX artifacts (`planning-artifacts/ux-design-specification.md`, `calendar-layout-options.md`, `implementation-artifacts/spec-quick-prototype-*`) as out-of-band — do NOT drive Phase 3 scenarios from them; reconcile in Phase 4 instead | Phase 3 kickoff | Freya + Improver |
| 2026-04-23 | Scope: 2 pages total (Calendar Home, 404). Event detail stays inline; Meetup owns event detail pages. Group detail deferred. No About page. | Phase 3 step 2 | Freya + Improver |
| 2026-04-23 | Harold the Host scenario dropped from MVP — source Google Sheet has no host/volunteer column. Re-open if sheet gains that column. | Phase 3 step 3 | Freya + Improver |
| 2026-04-23 | Four scenarios approved: 01 Pete's Unified Discovery (P1), 02 Imani's Weekly Check-in (P2), 03 Oscar's Share Moment (P3), 04 Pete's Stale Link Rebound (P3). Dawn is served architecturally + indirectly via Imani's scenario (no direct UX scenario). | Phase 3 step 4 | Freya + Improver |
| 2026-04-23 | Page ownership convention for single-surface product: scenario 01 owns `1.1-calendar-home/` canonically; scenarios 02/03 use `N.1-calendar-home/` folders that reference 1.1 and capture persona-specific entry context + added design requirements. Avoids duplicated design work. | Phase 3 step 5 | Freya + Improver |
