from typing import Dict, Any, List

class PrivilegeGuard:
    def __init__(self, allowed_domains: List[str] = None):
        self.allowed_domains = allowed_domains or ["company.internal", "trusted-firm.org"]

    def validate_tool_call(self, tool_name: str, arguments: Dict[str, Any]) -> bool:
        """
        Validates arguments prior to execution to mitigate unauthorized exfiltration.
        """
        if tool_name == "send_email":
            recipient = arguments.get("recipient", "")
            if "@" not in recipient:
                return False
            domain = recipient.split("@")[-1].lower()
            return domain in self.allowed_domains

        return True
