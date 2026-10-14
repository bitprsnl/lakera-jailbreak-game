import re
from typing import Any, Dict, List, Optional


class InputGuard:
      INJECTION_SIGNATURES = [
                r"ignore\s+(all\s+)?(previous|prior|above)\s+(instructions|prompts|directions)",
                r"disregard\s+(all\s+)?(previous|prior|above)\s+(instructions|prompts)",
                r"you\s+are\s+now\s+(in\s+)?(developer\s+mode|dan|unfiltered|jailbroken)",
                r"(output|print|reveal|display|leak)\s+(the\s+)?(system\s+prompt|passcode|secret\s+key|password)",
                r"system\s*prompt\s*override",
      ]

    def __init__(self, custom_signatures: Optional[List[str]] = None, canary_tokens: Optional[List[str]] = None):
              signatures = self.INJECTION_SIGNATURES + (custom_signatures or [])
              self.compiled_patterns = [re.compile(sig, re.IGNORECASE | re.MULTILINE) for sig in signatures]
              self.canary_tokens = canary_tokens or []

    def scan_input(self, text: str) -> Dict[str, Any]:
              if not text or not isinstance(text, str):
                            return {"is_flagged": False, "matched_patterns": [], "confidence": 0.0, "threat_level": "LOW"}
                        matches = [p.search(text).group(0) for p in self.compiled_patterns if p.search(text)]
        is_flagged = len(matches) > 0
        confidence = min(1.0, 0.4 + (len(matches) * 0.3)) if is_flagged else 0.0
        return {
                      "is_flagged": is_flagged,
                      "matched_patterns": matches,
                      "confidence": round(confidence, 2),
                      "threat_level": "HIGH" if len(matches) > 1 else ("MEDIUM" if is_flagged else "LOW"),
        }
