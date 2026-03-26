# ADR-005: Credentials Management

**Status:** Accepted
**Date:** 2026-03-26

## Decision

All secrets (Google service account key, Slack webhook URL, Healthchecks.io ping URL) are stored in Azure Key Vault and injected into the Azure Function at runtime.

## Rationale

- No secrets in the repository
- Azure Key Vault is consistent with Improving's existing Azure footprint
- Key rotation does not require code changes
