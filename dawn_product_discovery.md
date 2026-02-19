# Product Discovery: User Group Management Tool
**Subject Matter Expert:** Dawn Dearstone, Administrative Assistant  
**Context:** Internal tool to support management of community-hosted user groups at Improving  
**Purpose:** Structured discovery notes for product management — vision, direction, and prioritization input

---

## Overview

Improving hosts community-led user groups by providing space, food, and drinks. External organizers run the groups themselves. Dawn — as Executive Assistant to the CEO — serves as the internal point of contact responsible for coordinating logistics: volunteer host scheduling, headcount for catering, and day-of coordination. Given her seniority and the breadth of her responsibilities supporting the CEO, the tool should be especially mindful of minimizing her time investment. The goal is to reduce friction in these recurring, low-complexity but time-consuming workflows so that Dawn's attention can remain focused on higher-order executive support.

---

## Persona

**Name:** Dawn Dearstone  
**Role:** Executive Assistant to the CEO  
**Technical Comfort:** Moderate — comfortable with Google Sheets, email, and Meetup.com  
**Motivation:** Efficiency and reliability over sophistication. Prefers simple, stable workflows (e.g., "one never-changing link").  
**Disposition:** Pragmatic. Pleasantly surprised when things are easier than expected. Frustrated by tasks that feel like herding cats (e.g., chasing signups). As an EA to the CEO, her time is high-value — any tool that requires active management is a liability, not an asset.

---

## Current Workflow (As-Is)

### Recurring Responsibilities

| Task | Frequency | Tool Used | Notes |
|------|-----------|-----------|-------|
| Maintain host volunteer calendar | Annually + monthly reminders | Google Sheet | Sheet rarely fills up; gaps remain |
| Send host signup link | Monthly (email blast) | Email | One static link; easy |
| Contact organizer for headcount | Day-of (or day before) | Email/phone | Varies by organizer reliability |
| Order pizza from Pizza Hut | Per event | Phone/online | Based on headcount; standard mix with minor per-group variation |
| Post-event cleanup coordination | Next day (if needed) | Manual | Chairs and room state are common issues |

### Food & Catering

Pizza Hut is the established vendor for all user group events. The order is fairly standardized, built around a core mix that covers common dietary needs:

- **Standard mix:** Cheese, pepperoni, supreme, and at least one veggie option
- **Per-group adjustments:** Some groups request more vegetarian-friendly options; others skew toward meat-heavy. These are minor variations on the same base formula — nothing custom or complex.
- **Driver:** Headcount from the organizer determines order size. Dietary preference variations are either communicated by the organizer or inferred from group identity.

> **Opportunity:** A simple pizza calculator or order template tied to headcount and group preference profile could eliminate guesswork and standardize ordering. Pre-saved order profiles per user group would allow one-click (or zero-click) order generation.

### External Dependencies
- User groups are organized by external parties via **Meetup.com**
- Organizers handle their own group promotion and attendance
- Some organizers (e.g., Stewart, Unix group) proactively send headcount — Dawn values this
- **Pizza Hut** is the sole food vendor — relationship is established and consistent; no vendor selection or comparison needed

---

## Pain Points (Problems to Solve)

### P1 — Volunteer Host Signup Gaps *(High friction, recurring)*
The Google Sheet calendar for volunteer hosts never fully fills. Dawn must personally follow up to fill remaining slots. This is the most emotionally taxing task — equivalent to "begging."

> **Opportunity:** Proactive reminders, gamification, or visibility tools to drive signup completion without manual intervention.

### P2 — Room Setup is the Most Time-Intensive Task *(Operational burden)*
Setting up the room before each event is the single largest time sink. Cleanup after events (displaced chairs, general tidying) adds next-day burden.

> **Opportunity:** Checklist tooling, volunteer accountability, or pre/post event task delegation features.

### P3 — Inconsistent Headcount Communication *(Day-of risk)*
Organizers vary widely in how proactively they communicate attendance. Day-of headcount requests add last-minute stress.

> **Opportunity:** Automated headcount request workflows sent to organizers N days before the event.

### P4 — Attendees Show Up to Cancelled Events *(Experience and reputational risk)*
Occasionally, users arrive unaware that a group was cancelled. There is no reliable mechanism to communicate cancellations externally.

> **Opportunity:** Cancellation notification system (email, Meetup sync, or public-facing calendar update).

### P5 — No Public Digital Calendar *(Low priority for Dawn, but visible gap)*
A public-facing list of hosted user groups previously existed but is no longer active. Dawn notes this doesn't directly impact her, but it's a recognized gap.

> **Opportunity:** Low-effort integration or display widget for the company website — not a Dawn problem, but a product/marketing consideration.

---

## What's Working Well (Preserve in Product Design)

- **Static link model:** Dawn loves that the Google Sheet link never changes. Any tool should provide stable, bookmarkable URLs or entry points.
- **External organizer autonomy:** Dawn does not manage the content or logistics of the groups themselves — the tool should not add that burden.
- **Low-touch calendar maintenance:** Annual setup with monthly nudges works well in principle; the problem is compliance, not the cadence.
- **Organizer-led promotion:** Meetup.com handles external visibility adequately. Integration should be read-only or notification-based, not a replacement.

---

## Jobs to Be Done (JTBD)

1. **When** volunteer host slots are unfilled, **Dawn needs to** get employees to sign up **without** personally chasing each one.
2. **When** a user group is approaching, **Dawn needs to** know the expected headcount **without** initiating the request herself day-of.
3. **When** a user group is cancelled, **Dawn needs to** ensure attendees are notified **without** manual outreach.
5. **When** headcount is confirmed, **Dawn needs to** place a Pizza Hut order **without** having to manually calculate quantities or recall each group's preferences.

---

## Suggested Product Principles (Derived from Discovery)

- **Reduce herding:** Automate reminders and requests rather than relying on Dawn to chase people.
- **Stable interfaces:** Avoid frequently changing URLs, forms, or workflows. Dawn values consistency.
- **Minimal new burden:** Dawn is an EA to the CEO — her bandwidth is finite and her priorities are executive-level. The tool must absorb tasks, not create new ones. Any feature that requires active management by Dawn is a design failure.
- **Graceful fallback:** Dawn currently covers gaps herself. The tool should make gaps visible early, not just at the last minute.
- **Organizer-friendly nudges:** Build lightweight touchpoints for external organizers (headcount requests, cancellation confirmations) that don't require them to adopt new software.

---

## Out of Scope (Per Discovery)

- Content or agenda management for user groups (handled by external organizers)
- Meetup.com group administration
- Public-facing calendar (Dawn's explicit deprioritization)

---

## Open Questions for Product Management

1. Who else interacts with this workflow? (e.g., office manager, facilities, reception)
2. Is there a budget cap or approval process for Pizza Hut orders, and does it vary by group size or event type?
3. What is the current volume? (number of user groups per month, frequency per group)
4. Are there other admins or backup personnel when Dawn is unavailable?
5. Should the tool notify employees about upcoming user groups to drive internal attendance?
6. Is there appetite to resurface the public-facing calendar, and if so, who owns that?
