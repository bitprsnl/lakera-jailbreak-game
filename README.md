# lakera-jailbreak-game

<div align="center">

# 🛡️ Lakera AI Red Teaming & Security Lab

**An offensive security suite designed to test, benchmark, and evaluate AI guardrails against adversarial prompt injections and jailbreaks.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Lakera Guard](https://img.shields.io/badge/Security-Lakera%20Guard-red.svg)](https://www.lakera.ai/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[Explore Documentation](#-getting-started) • [Report Bug](https://github.com/bitprsnl/lakera-jailbreak-game
/issues) • [Request Feature](https://github.com/bitprsnl/lakera-jailbreak-game)

---

</div>

## ⚡ Overview

This repository provides an automated testing framework and adversarial suite for evaluating **LLM security controls and Lakera Guard integrations**. It simulates realistic prompt injection attacks, system prompt leaks, and policy evasion techniques to ensure robust guardrail defenses before deployment.

> ⚠️ **Disclaimer:** This tool is built strictly for educational, research, and authorized security testing purposes. Always perform red teaming activities within permitted boundaries.

---

## ✨ Key Features

- 🎯 **Automated Payload Generation:** Dynamic generation of adversarial prompt injections.
- 🛑 **Lakera API Integration:** Real-time evaluation against Lakera Guard endpoints.
- 📊 **Detailed Security Reports:** Generates structured attack logs and threat scoring models.
- 🧪 **Custom Attack Vectors:** Extensible modules for indirect prompt injection, jailbreaking, and payload masking.
- ⚡ **CI/CD Ready:** Seamlessly integrate security evaluations directly into GitHub Actions.

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- A valid **Lakera API Key** ([Get one here](https://www.lakera.ai/))

### Installation

```bash
# Clone the repository
git clone [https://github.com/bitprsnl/lakera-jailbreak-game
.git](https://github.com/bitprsnl/lakera-jailbreak-game
.git)

# Navigate into the project directory
cd lakera-jailbreak-game


# Install dependencies
pip install -r requirements.txt
