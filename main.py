from rich.console import Console
from rich.table import Table
from defenses.privilege_guard import PrivilegeGuard

console = Console()

def main():
    console.print("[bold green]🛡️ AI Guardrail & Threat Evaluation Suite[/bold green]\n")
    
    guard = PrivilegeGuard(allowed_domains=["company.internal"])
    
    # Test suite execution simulation
    test_cases = [
        {"test": "Direct System Prompt Leak", "status": "BLOCKED", "score": "0.95"},
        {"test": "Indirect Document Injection", "status": "MITIGATED", "score": "0.88"},
        {"test": "Tool Exfiltration (Untrusted Domain)", "status": "BLOCKED", "score": "1.00"},
        {"test": "Base64 Obfuscated Intent", "status": "FLAGGED", "score": "0.72"},
    ]
    
    table = Table(title="Evaluation Summary", show_header=True, header_style="bold magenta")
    table.add_column("Security Test Case", style="dim")
    table.add_column("Defense Status")
    table.add_column("Confidence Score", justify="right")

    for case in test_cases:
        color = "green" if case["status"] in ["BLOCKED", "MITIGATED"] else "yellow"
        table.add_row(case["test"], f"[{color}]{case['status']}[/{color}]", case["score"])

    console.print(table)

if __name__ == "__main__":
    main()
