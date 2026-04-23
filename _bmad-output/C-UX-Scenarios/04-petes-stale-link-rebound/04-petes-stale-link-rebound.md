# 04: Pete's Stale Link Rebound

**Project:** air-pods-cohort-1
**Created:** 2026-04-23
**Method:** Whiteport Design Studio (WDS)
**Priority:** 3

---

## Transaction (Q1)

**What this scenario covers:**
Recover from landing on a URL that doesn't exist — without losing trust or abandoning the visit.

---

## Business Goal (Q2)

**Primary Goal:** BG1 — Maximize Community Visibility
**Objective:** 3+ external referral sources within 3 months. Every rescued 404 preserves the ROI of a hard-won referral. A visitor lost at a broken URL is a referral that cashed out at zero.

**Secondary Goal:** BG2 — Increase Event Attendance
**Objective:** 30%+ click-through from calendar to Meetup. Rescued visitors rejoin the Pete-01 flow and still have a chance to convert.

---

## User & Situation (Q3)

**Persona:** Prospective Pete (Primary / P1 — stand-in for any mistyped-URL or stale-index visitor; first-time visitors hit 404s more than returning ones)

**Situation:** Same Pete as scenario 01, but his LinkedIn app mangled the URL on paste, or the post is months old and references a path that's since changed, or he's clicking a Google result whose index hasn't caught up to a URL change. He's on mobile, mid-scroll, expecting the Improving calendar — lands on a 404 instead.

---

## Driving Forces (Q4)

**Hope:** Get to the thing he was promised despite a bad URL.

**Worry:** The whole calendar is vaporware; this was a waste of a tap; he closes the tab and doesn't try again.

---

## Device & Starting Point (Q5 + Q6)

**Device:** Mobile (iPhone — highest-risk device for typos, stale shares, and bounce)

**Entry:** Tapped a shared link from LinkedIn on mobile. URL was mangled or stale. Expected Calendar Home; got 404.

---

## Best Outcome (Q7)

**User Success:**
Sees a friendly 404 that explains the page is missing and offers one obvious next action; taps it; lands on Calendar Home; continues with scenario 01's flow.

**Business Success:**
First-time visitor rescued, not lost. Referral-source ROI preserved (BG1). Visitor gets a chance to convert to the Meetup click-through (BG2).

---

## Shortest Path (Q8)

1. **404** — Pete lands on a friendly 404. Copy is warm and self-explanatory: *"This page doesn't exist — but the Improving Community Calendar does."* Single CTA: "Go to the calendar." Identity anchor visible. Taps the CTA.
2. **Calendar Home** — Pete rejoins scenario 01's flow. ✓

Scenario 04 success is the rebound itself — the moment Pete arrives on Calendar Home. What happens next on Calendar Home is scenario 01's job.

---

## Trigger Map Connections

**Persona:** Prospective Pete (Primary / P1, as a generic first-time-visitor stand-in)

**Driving Forces Addressed:**
- ❌ **Fear:** -14 *Fragmented discovery frustration* — sharply amplified if the ONE URL he has fails. A 404 feels like fragmentation all over again.

**Business Goals:**
- **BG1 Maximize Community Visibility** — preserves the ROI of rare first-time visits
- **BG2 Increase Event Attendance** — rescued visitors rejoin the conversion flow

---

## Scenario Steps

| Step | Folder | Purpose | Exit Action |
|------|--------|---------|-------------|
| 4.1 | `4.1-not-found/` | Reassure, anchor identity, offer single obvious CTA | Taps "Go to the calendar" → rejoin scenario 01 |
| 4.2 | *rejoin scenario 01 at `1.1-calendar-home`* | Success condition satisfied; rest of the journey is scenario 01's | Scenario success ✓ |

**First step (4.1)** includes full entry context (Q3 + Q4 + Q5 + Q6).

**Note:** Step 4.2 is not an independently-owned page — it is a handoff back to the Calendar Home canonically designed in `1.1-calendar-home/`. No separate page folder is created for step 4.2 to avoid design-artifact duplication.
