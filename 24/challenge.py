from abc import ABC, abstractmethod
from typing import Any


class Challenge(ABC):
    def __init__(self, number: int, title: str):
        self.number = number
        self.title = title

    @property
    @abstractmethod
    def pretty_title(self):
        pass

    @abstractmethod
    def verify(self, value: Any):
        pass


class BlogChallenge(Challenge):
    def __init__(self, number: int, title: str, merged_prs: int):
        super().__init__(number, title)
        self.merged_prs = merged_prs

    @property
    def pretty_title(self):
        return f"PCC{self.number} - {self.title}"

    def verify(self, value: Any):
        return value in [41, 42, 44]


class BiteChallenge(Challenge):
    def __init__(self, number: int, title: str, result: str):
        super().__init__(number, title)
        self.result = result

    @property
    def pretty_title(self):
        return f"Bite {self.number}. {self.title}"

    def verify(self, value: Any):
        return value == "my result"
