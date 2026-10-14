from typing import Any, Dict, List, Optional
from urllib.parse import urlparse


class PrivilegeGuard:
      DEFAULT_ALLOWED_DOMAINS = ["company.com", "partner.org"]
      DEFAULT_BLOCKED_COMMANDS = ["rm -rf", "mkfs", "dd", "chmod 777", "> /dev/", ":(){ :|:& };:"]

    def __init__(
              self,
              allowed_domains: Optional[List[str]] = None,
              allowed_tools: Optional[List[str]] = None,
              blocked_commands: Optional[List[str]] = None,
    ):
              self.allowed_domains = [d.lower() for d in (allowed_domains or self.DEFAULT_ALLOWED_DOMAINS)]
              self.allowed_tools = allowed_tools
              self.blocked_commands = blocked_commands or self.DEFAULT_BLOCKED_COMMANDS

    def validate_tool_call(self, tool_name: str, arguments: Optional[Dict[str, Any]] = None) -> bool:
              return self.inspect_tool_call(tool_name, arguments)["allowed"]

    def inspect_tool_call(self, tool_name: str, arguments: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
              args = arguments or {}
              if self.allowed_tools is not None and tool_name not in self.allowed_tools:
                            return {"allowed": False, "tool_name": tool_name, "reason": "Tool not in whitelist."}

              if tool_name in ("send_email", "email_tool", "dispatch_mail"):
                            raw = args.get("to") or args.get("recipient") or args.get("recipients") or []
                            recipients = [addr.strip() for addr in raw.split(",") if addr.strip()] if isinstance(raw, str) else list(raw)
                            if not recipients:
                                              return {"allowed": False, "tool_name": tool_name, "reason": "Missing recipient."}
                                          for r in recipients:
                                                            if "@" not in r:
                                                                                  return {"allowed": False, "tool_name": tool_name, "reason": "Invalid email."}
                                                                              domain = r.split("@")[-1].strip().lower()
                                                            if not any(domain == d or domain.endswith("." + d) for d in self.allowed_domains):
                                                                                  return {"allowed": False, "tool_name": tool_name, "reason": "Unauthorized domain."}

              elif tool_name in ("http_request", "fetch_url", "web_request", "curl"):
                            url = str(args.get("url") or args.get("endpoint") or "")
                            hostname = (urlparse(url).hostname or "").lower()
                            if not hostname or not any(hostname == d or hostname.endswith("." + d) for d in self.allowed_domains):
                                              return {"allowed": False, "tool_name": tool_name, "reason": "Unauthorized URL."}

elif tool_name in ("execute_bash", "run_command", "shell", "exec"):
            cmd = str(args.get("command") or args.get("cmd") or "")
            if any(b in cmd for b in self.blocked_commands):
                              return {"allowed": False, "tool_name": tool_name, "reason": "Blocked command."}

elif tool_name in ("read_file", "write_file", "delete_file"):
              path = str(args.get("path") or args.get("file_path") or "")
              if ".." in path or path.startswith("/etc/") or path.startswith("/root/"):
                                return {"allowed": False, "tool_name": tool_name, "reason": "Path traversal blocked."}

          return {"allowed": True, "tool_name": tool_name, "reason": "Policy check passed."}
