from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseEvaluator(ABC):
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    @abstractmethod
    def run_test(self, agent) -> Dict[str, Any]:
        """
        Executes test against the agent harness and returns structured metric dict.
        """
        pass
