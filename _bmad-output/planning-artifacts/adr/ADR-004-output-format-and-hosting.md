# ADR-004: Output Format and Hosting

**Status:** Accepted
**Date:** 2026-03-26

## Decision

Pipeline output is a single `events.json` file published to Azure Blob Storage, served at a stable Improving subdomain.

## Rejected Alternative

Generating static HTML in the pipeline.

## Rationale

- JSON decouples data from presentation — the pipeline has one job; rendering is a separate concern owned by a separate layer
- Multiple consumers can read `events.json` without changes to the pipeline (web frontend, mobile app, future integrations)
- Azure Blob Storage with a CDN/custom domain provides stable URL, fast delivery, and 99%+ availability without managing a server
- Subdomain (`events.improving.com` or similar) satisfies the stable URL requirement and keeps the URL within Improving's domain

## Scope Boundary

SEO is not a concern of the data pipeline. It is the responsibility of the presentation layer that consumes `events.json`. The pipeline's contract is well-structured, reliable JSON — not rendered HTML.

## IT Action Required

DNS configuration to point the subdomain at the Blob Storage public endpoint.
