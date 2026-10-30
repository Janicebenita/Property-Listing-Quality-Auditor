# Property Listing Quality Auditor Explainability

## Decision and Reasoning Process

The agent's decision process checks required fields, cross-field consistency, wording quality, and evidence for material claims. Its reasoning explains every flagged issue and the checklist rule that triggered it.

## Inputs and Data Sources Used

Input data includes draft listing text, property specifications, approved photos or captions, seller-provided information, and the quality checklist. Official records are used only when authorized as data sources.

## Outputs and Supporting Evidence

The output lists missing fields, contradictions, risky claims, clarity improvements, and verification actions. Each issue is linked to the relevant listing field or reference record.

## Limits, Constraints, and Known Issues

A limitation is that the agent cannot independently verify ownership, title, structural condition, approvals, or legal compliance. It is constrained from presenting uncertain information as fact.

## Uncertainty and Human Review

Uncertainty is highlighted when records conflict or verification is unavailable. Human approval is required before the listing is published or amended.

## Implementation in This Repository

`agent.py` implements `audit_listing(listing)`. It checks the declared `REQUIRED_FIELDS`, scans the description for four `CLAIMS_REQUIRING_EVIDENCE`, distinguishes missing fields from unsupported claims, retains the supplied listing fields as evidence, never approves publication, and requires human review. `test_agent.py` verifies both issue types and the publication guardrail.

No property-registry, publication, or listing-edit API is implemented. A human alone may verify facts or publish changes.
