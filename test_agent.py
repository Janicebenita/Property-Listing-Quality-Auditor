import unittest
from agent import audit_listing


class ListingTests(unittest.TestCase):
    def test_unsupported_claim_and_missing_fields_are_visible(self):
        result = audit_listing({"id": "L1", "description": "Guaranteed return"})
        types = {issue["type"] for issue in result["issues"]}
        self.assertEqual(types, {"missing-field", "unsupported-claim"})
        self.assertFalse(result["publication_approved"])


if __name__ == "__main__":
    unittest.main()
