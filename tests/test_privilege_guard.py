import unittest
from defenses.privilege_guard import PrivilegeGuard


class TestPrivilegeGuard(unittest.TestCase):
        def setUp(self):
                    self.guard = PrivilegeGuard(allowed_domains=["company.com", "partner.org"])

        def test_whitelisted_domain_allowed(self):
                    self.assertTrue(self.guard.validate_tool_call("send_email", {"to": "security@company.com"}))
                    self.assertTrue(self.guard.validate_tool_call("send_email", {"to": "audit@partner.org"}))

        def test_unauthorized_domain_blocked(self):
                    self.assertFalse(self.guard.validate_tool_call("send_email", {"to": "attacker@evil.com"}))

        def test_subdomain_handling(self):
                    self.assertTrue(self.guard.validate_tool_call("send_email", {"to": "admin@sub.company.com"}))
                    self.assertFalse(self.guard.validate_tool_call("send_email", {"to": "admin@notcompany.com"}))


if __name__ == "__main__":
        unittest.main()
