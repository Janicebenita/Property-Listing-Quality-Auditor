"""Audit supplied property-listing fields and unsupported marketing claims."""
from __future__ import annotations

REQUIRED_FIELDS = ("title", "price", "location", "property_type", "bedrooms", "description", "contact")
CLAIMS_REQUIRING_EVIDENCE = ("guaranteed return", "legally approved", "best investment", "zero risk")


def audit_listing(listing: dict) -> dict:
    missing = [field for field in REQUIRED_FIELDS if listing.get(field) in (None, "", [])]
    description = str(listing.get("description", "")).lower()
    unsupported = [claim for claim in CLAIMS_REQUIRING_EVIDENCE if claim in description and claim not in {str(value).lower() for value in listing.get("verified_claims", [])}]
    issues = ([{"type": "missing-field", "field": field} for field in missing] + [{"type": "unsupported-claim", "claim": claim} for claim in unsupported])
    return {"listing_id": listing.get("id"), "status": "review" if issues else "structurally-complete", "issues": issues, "evidence": {field: listing.get(field) for field in REQUIRED_FIELDS}, "publication_approved": False, "human_review_required": True}
