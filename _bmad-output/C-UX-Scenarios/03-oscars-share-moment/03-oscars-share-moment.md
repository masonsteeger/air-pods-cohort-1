# 03: Oscar's Share Moment

**Project:** air-pods-cohort-1
**Created:** 2026-04-23
**Method:** Whiteport Design Studio (WDS)
**Priority:** 3

---

## Transaction (Q1)

**What this scenario covers:**
Verify the calendar is credible enough to put his name behind, then copy the URL to share in his own community channels.

---

## Business Goal (Q2)

**Primary Goal:** BG1 — Maximize Community Visibility
**Objective:** 3+ external referral sources within 3 months. Oscar's share *is* one of those referrals — this scenario directly delivers the BG1 metric.

**Secondary Goal:** BG2 — Increase Event Attendance
**Objective:** Oscar's newsletter recipients become Pete-style discoverers downstream, feeding the CTR flywheel.

---

## User & Situation (Q3)

**Persona:** Oscar the Organizer (Tertiary / P4)

**Situation:** Volunteer who runs a DFW meetup at Improving's space. Passionate but stretched thin — his growth constraint is reach, not content. It's Saturday afternoon and he's composing his monthly email to his group's mailing list (a task he finds draggy). An Improving announcement in his Slack mentioned the public calendar is live. He thinks: *I could include this as the "here's the rest of the community" anchor in my newsletter.* Before he shares it, he wants to verify it doesn't make him look bad.

---

## Driving Forces (Q4)

**Hope:** Confirm his group is listed accurately and the page looks professional enough to represent his community.

**Worry:** His group is missing or misnamed, or the page looks amateur, and sharing it would reflect poorly on him.

---

## Device & Starting Point (Q5 + Q6)

**Device:** Desktop (Mac, Chrome — he's at his laptop composing a newsletter)

**Entry:** Clicked the link from Improving's announcement in his Slack. Landed on Calendar Home. An inspection visit, not a discovery visit.

---

## Best Outcome (Q7)

**User Success:**
Oscar verifies his group and upcoming events are listed correctly; the page has a visible "Improving Community Calendar" identity anchor so recipients know what it is; he copies the stable URL from the address bar and pastes it into his newsletter with a line like "See the full Improving community calendar here."

**Business Success:**
Oscar becomes one of the 3+ external referral sources (BG1 metric satisfied in one stroke). His newsletter propagates the URL to 100+ group members, seeding future Pete-style discovery traffic (BG2 downstream).

---

## Shortest Path (Q8)

1. **Calendar Home** — Oscar lands, scrolls to find his group's upcoming events, verifies the listing matches his Meetup page, notes the Improving brand identity is visible, copies the URL from the browser address bar. Closes the tab and returns to his newsletter. ✓

---

## Trigger Map Connections

**Persona:** Oscar the Organizer (Tertiary / P4)

**Driving Forces Addressed:**
- ✅ **Want:** +12 *Free discovery channel for new members*
- ✅ **Want:** +11 *Shareable umbrella link*
- ❌ **Fear:** -12 *Frustration with invisible community investment*
- ❌ **Fear:** -11 *Fear of inaccurate listing*

**Business Goals:**
- **BG1 Maximize Community Visibility** — Oscar's share is the referral source (direct metric delivery)
- **BG2 Increase Event Attendance** — downstream, via Oscar's newsletter recipients

---

## Design Requirements This Scenario Imposes on Calendar Home

Calendar Home is owned and documented in scenario 01. This scenario adds:

1. **Identity anchor** — a visible "Improving Community Calendar" header/branding. Oscar only shares if his recipients will understand what they're clicking into. Neutral URL + branded page = Oscar shares. Neutral URL + unbranded page = Oscar doesn't share.
2. **Find-my-group scanability** — group names must be visible on every row. No group-filter in MVP, so scroll-scan must work.
3. **URL stability** — the URL copied from the address bar must be canonical, stable, and free of per-session tokens or variable query params. Already specified in the brief as non-negotiable.
4. **Low-cost enhancement (optional):** OG meta tags so the URL expands to a nice preview when pasted into Slack/email/LinkedIn. Not MVP-critical but addresses Oscar's "looks amateur" fear cheaply.

---

## Scenario Steps

| Step | Folder | Purpose | Exit Action |
|------|--------|---------|-------------|
| 3.1 | `3.1-calendar-home/` | Verify group listing accuracy; copy stable URL for sharing | Copies URL from address bar; closes tab — scenario success ✓ |

**First step (3.1)** includes full entry context (Q3 + Q4 + Q5 + Q6).

**Note:** The page design is owned by `1.1-calendar-home/` (scenario 01). The `3.1-calendar-home/` spec captures Oscar's scenario-specific context and the design requirements his scenario adds. In Phase 4, page design work happens once in 1.1; 3.1 is consulted to ensure Oscar's requirements are honored.
