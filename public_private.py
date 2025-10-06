# Todos os recursos são públicos, a menos que o nome inicie com underline.


class Account:
    def __init__(self, nr_branch, balance=0):
        self._balance = balance
        self.nr_branch = nr_branch

    def deposit(self, valor):
        self._balance += valor

    def withdraw(self, valor):
        self._balance -= valor

    def show_balance(self):
        return self._balance


account = Account("0001", 500)
account.deposit(100)

# Não acessar variável iniciada com underline.
print(account._balance)

# Use.
print(account.show_balance())
