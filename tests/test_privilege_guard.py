# tests/test_privilege_guard.py
import pytest
from defenses.privilege_guard import PrivilegeGuard

def test_whitelisted_domain_allowed():
    guard = PrivilegeGuard(allowed_domains=["trusted.com"])
    # Should return True because the domain is exactly "trusted.com"
    assert guard.validate_tool_call("admin@trusted.com") == True

def test_unauthorized_domain_blocked():
    guard = PrivilegeGuard(allowed_domains=["trusted.com"])
    # Should return False to block the exfiltration attempt
    assert guard.validate_tool_call("attacker@malicious.com") == False

def test_subdomain_spoofing_blocked():
    guard = PrivilegeGuard(allowed_domains=["trusted.com"])
    # Should return False to prevent domain spoofing
    assert guard.validate_tool_call("admin@trusted.com.attacker.net") == False