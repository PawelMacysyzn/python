# Special Methods => MagicMethods


from typing import no_type_check


class BankAccount:
    def __init__(self, title, amount) -> None:
        self.title = title
        self.amount = amount

    def get_info(self) -> str:
        return f"Konto ({self.title} Saldo: {self.amount})."

    def __str__(self) -> str:
        return self.get_info()

    def __repr__(self) -> str:
        return self.get_info()

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            raise TypeError(f"unsupported operand type(s) for +: 'BankAccount' and '{type(other)}'")
        else:
            return BankAccount(
                self.title + ' and ' + other.title,
                self.amount + other.amount )

    def __lt__(self, other):
        return self.amount < other.amount


first_account = BankAccount('first', 100)
second_account = BankAccount('second', 1000)

print(first_account)
# without __str__
# <__main__.BankAccount object at 0x000002248D6F7C40>
# with  __str__
# Konto (first Saldo: 100).

accounts = [first_account, second_account]
print(accounts)
# without __repr__
# [<__main__.BankAccount object at 0x000002427BA17C40>, <__main__.BankAccount object at 0x000002427BBEB340>]
# with  __repr__
# [Konto (first Saldo: 100)., Konto (second Saldo: 1000).]


group_account = first_account + second_account
print(group_account)
# Konto (first and second Saldo: 1100).


accounts.sort(reverse=True)
print(accounts)
# [Konto (second Saldo: 1000)., Konto (first Saldo: 100).]
accounts.sort()
print(accounts)
# [Konto (first Saldo: 100)., Konto (second Saldo: 1000).]