class UserBankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = value
        print("executing setter")

    @property
    def account_holder(self):
        return self._account_holder

    @account_holder.setter
    def account_holder(self, value):
        self._account_holder = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance cannot be negative")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, Balance: {self.balance})"

    def copy(self):
        new_account = UserBankAccount(self.account_number, self.account_holder, self.balance)
        return new_account

