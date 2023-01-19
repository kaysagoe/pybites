from typing import Union


class Account:
    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __add__(self, other: Union[int, float]) -> None:
        if type(other) is not int and type(other) is not float:
            raise TypeError(
                "Only numeric values can be added to instance of type Account"
            )
        self._transactions.append(other)

    def __sub__(self, other: Union[int, float]) -> None:
        if type(other) is not int and type(other) is not float:
            raise TypeError(
                "Only numeric values can be added to instance of type Account"
            )
        self._transactions.append(-other)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __len__(self) -> int:
        return len(self._transactions)

    def __getitem__(self, key: int) -> Union[int, float]:
        return self._transactions[key]

    def __str__(self) -> str:
        return f"{self.name} account - balance: {self.balance}"
