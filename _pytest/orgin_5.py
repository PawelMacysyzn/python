'''
Development of the orgin_3.py task:

Test a situation in which you withdraw more than possible.

EN/PL

Rozwinięcie zadania orgin_3.py:

Przetestuj sytuacji w której wypłacasz więcej niz to możliwe.
'''

import pytest


class Bank:
    def __init__(self) -> None:
        self.amount = 0

    def add_money(self, money: int):
        self.amount += money

    def withdraw_money(self, money: int):
        if money > self.amount:
            raise NotEnoughCash('Not enough cash...')
        self.amount -= money

        return money


class NotEnoughCash(Exception):
    pass


class TestBank:
    def test_withdraw_over_amount(self):
        with pytest.raises(NotEnoughCash):
            bank = Bank()
            bank.withdraw_money(200)
