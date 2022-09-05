'''
Prepare a Bank class. Which should be able to deposit and withdraw. At the time of initialization, the bank should contain an empty balance.

Do not test a situation in which you deposit more than possible.

EN/PL

Przygotuj klasę Bank. Która powinna mieć mozliwośc wpłacania oraz wypłacanioa. W chwili inicjalizacji bank powinnien zawierac puste salto.

Nie testuj sytułacji w której wpłacasz więcej niz to możliwe.
'''


class Bank:
    def __init__(self) -> None:
        self.amount = 0

    def add_money(self, money: int):
        self.amount += money

    def withdraw_money(self, money: int):
        self.amount -= money

        return money


class TestBank:

    def test_create_bank(self):
        bank = Bank()
        assert bank.amount == 0
        assert isinstance(bank, Bank)

    def test_add_money(self):
        # given
        bank = Bank()

        # when
        bank.add_money(100)

        # then
        assert bank.amount == 100

    def test_add_money_twice(self):
        # given
        bank = Bank()

        # when
        bank.add_money(100)
        bank.add_money(100)

        # then
        assert bank.amount == 200

    def test_withdraw_money(self):
        # given
        bank = Bank()
        bank.add_money(100)

        # when
        money = bank.withdraw_money(100)

        # then
        assert money == 100
        assert bank.amount == 0
