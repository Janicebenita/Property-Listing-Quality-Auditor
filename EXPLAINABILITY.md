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

The implemented artifact is an OpenGAP declaration composed of `agent.yaml`, `SOUL.md`, this explainability file, and `README.md`. The manifest defines the listing fields and evidence to inspect, while the policy documents require the output to identify missing, conflicting, or unverified claims.

No property-registry, publication, or listing-edit API is implemented. A compatible host must present the audit findings and source evidence to a human, who alone may verify facts or publish changes.
