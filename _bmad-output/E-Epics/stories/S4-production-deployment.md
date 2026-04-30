# S4: Production Deployment

**Epic:** 01 — Public Event Calendar MVP
**Priority:** P1
**Estimate:** S
**Status:** Ready

---

## User Story

**As a** user
**I want** the calendar at a stable, shareable URL
**So that** I can bookmark it and share with others

---

## Acceptance Criteria

- [ ] Deployed to production URL
- [ ] URL is clean (no session tokens or query params)
- [ ] HTTPS enabled
- [ ] `/events` endpoint accessible
- [ ] `/` serves visual calendar
- [ ] Sync pipeline running on schedule

---

## Technical Notes

### Hosting Options

1. **Netlify** — Static site + serverless functions
2. **Vercel** — Static site + edge functions
3. **GitHub Pages** — Static only (sync via Actions)
4. **Cloudflare Pages** — Static + Workers

### URL Requirements

- Stable, memorable URL (e.g., `calendar.improving.com` or subdomain)
- No trailing slashes or redirects that break sharing
- Oscar's scenario: URL must look professional when pasted

### Deployment Checklist

- [ ] DNS configured
- [ ] SSL certificate provisioned
- [ ] Environment variables set (Google Sheets API key)
- [ ] Sync schedule configured
- [ ] Monitoring/alerting for sync failures

---

## References

- `planning-artifacts/ux-design-specification.md`
- Oscar's scenario — URL stability requirement
