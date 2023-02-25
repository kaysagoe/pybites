from collections import namedtuple
from datetime import datetime
from typing import List

Transaction = namedtuple(
    "Transaction", "giver points date", defaults=(None, None, datetime.now())
)


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self._transactions: List[Transaction] = list()

    @property
    def karma(self) -> int:
        return sum([trans.points for trans in self._transactions])

    @property
    def points(self) -> List[int]:
        return [trans.points for trans in self._transactions]

    @property
    def fans(self) -> int:
        return len({trans.giver for trans in self._transactions})

    def __add__(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)

    def __str__(self) -> str:
        return f"{self.name} has a karma of {self.karma} and {self.fans} {'fan' if self.fans == 1 else 'fans'}"
