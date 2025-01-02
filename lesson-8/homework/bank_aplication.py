import json

class Account:
    """
    A class to represent a bank account.

    Attributes:
    ----------
    account_number : int
        The account number of the account.
    name : str
        The name of the account holder.
    balance : float
        The balance of the account.
    """

    def __init__(self, account_number: int, name: str, initial_deposit: float = 0) -> None:
        """
        Constructs all the necessary attributes for the account object.

        Parameters:
        ----------
        account_number : int
            The account number of the account.
        name : str
            The name of the account holder.
        initial_deposit : float, optional
            The initial deposit amount (default is 0).
        """
        self.account_number = account_number
        self.name = name
        self.balance = initial_deposit

    @property
    def account_number(self) -> int:
        """Gets the account number."""
        return self._account_number

    @account_number.setter
    def account_number(self, value: int) -> None:
        """
        Sets the account number.

        Parameters:
        ----------
        value : int
            The account number to set.

        Raises:
        ------
        ValueError
            If the account number is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Account number must be a positive integer.")
        self._account_number = value

    @property
    def name(self) -> str:
        """Gets the name of the account holder."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Sets the name of the account holder.

        Parameters:
        ----------
        value : str
            The name to set.

        Raises:
        ------
        ValueError
            If the name is not a string, is empty, or contains non-alphabetic characters.
        """
        value = value.strip()
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if not value:
            raise ValueError("Name cannot be empty.")
        if not value.isalpha():
            raise ValueError("Name must contain only alphabetic characters.")
        self._name = value.capitalize()

    @property
    def balance(self) -> float:
        """Gets the balance of the account."""
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        """
        Sets the balance of the account.

        Parameters:
        ----------
        value : float
            The balance to set.

        Raises:
        ------
        ValueError
            If the balance is not a non-negative number.
        """
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Balance must be a non-negative number.")
        self._balance = float(value)

    def __str__(self) -> str:
        """Returns a string representation of the account."""
        return f"Account Number: {self.account_number}\nName: {self.name}\nBalance: {self.balance:.2f}"

    def to_dict(self) -> dict:
        """Converts the account object to a dictionary."""
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        """
        Creates an account object from a dictionary.

        Parameters:
        ----------
        data : dict
            The dictionary containing account data.

        Returns:
        -------
        Account
            The account object created from the dictionary.
        """
        return cls(data["account_number"], data["name"], data["balance"])


class Bank:
    """
    A class to represent a bank.

    Attributes:
    ----------
    accounts : dict[int, Account]
        A dictionary of accounts in the bank.
    """

    FILENAME = r"lesson-8/homework/accounts.json"

    def __init__(self):
        """Initializes the bank with accounts loaded from a file."""
        self.accounts = self._load_from_file()

    def _load_from_file(self) -> dict[int, Account]:
        """
        Loads accounts from a file.

        Returns:
        -------
        dict[int, Account]
            A dictionary of accounts loaded from the file.

        Raises:
        ------
        FileNotFoundError
            If the file is not found.
        json.JSONDecodeError
            If the file content is not valid JSON.
        """
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                return {int(acc_num): Account.from_dict(acc_data) for acc_num, acc_data in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_to_file(self) -> None:
        """Saves accounts to a file."""
        with open(self.FILENAME, "w") as file:
            data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
            json.dump(data, file, indent=4)

    def create_account(self, name: str, initial_deposit: float) -> None:
        """
        Creates a new account.

        Parameters:
        ----------
        name : str
            The name of the account holder.
        initial_deposit : float
            The initial deposit amount.
        """
        account_number = max(self.accounts.keys(), default=1000) + 1
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number: int) -> None:
        """
        Views an account.

        Parameters:
        ----------
        account_number : int
            The account number to view.

        Raises:
        ------
        ValueError
            If the account does not exist.
        """
        account = self._get_account(account_number)
        print(account)

    def deposit(self, account_number: int, amount: float) -> None:
        """
        Deposits an amount into an account.

        Parameters:
        ----------
        account_number : int
            The account number to deposit into.
        amount : float
            The amount to deposit.

        Raises:
        ------
        ValueError
            If the account does not exist or the amount is invalid.
        """
        account = self._get_account(account_number)
        account.balance += amount
        print(f"Deposited {amount:.2f}. New balance: {account.balance:.2f}")

    def withdraw(self, account_number: int, amount: float) -> None:
        """
        Withdraws an amount from an account.

        Parameters:
        ----------
        account_number : int
            The account number to withdraw from.
        amount : float
            The amount to withdraw.

        Raises:
        ------
        ValueError
            If the account does not exist, the amount is invalid, or there are insufficient funds.
        """
        account = self._get_account(account_number)
        if amount > account.balance:
            raise ValueError("Insufficient funds.")
        account.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {account.balance:.2f}")

    def _get_account(self, account_number: int) -> Account:
        """
        Gets an account by account number.

        Parameters:
        ----------
        account_number : int
            The account number to get.

        Returns:
        -------
        Account
            The account object.

        Raises:
        ------
        ValueError
            If the account does not exist.
        """
        if account_number not in self.accounts:
            raise ValueError("Account does not exist.")
        return self.accounts[account_number]


def parse_input(prompt: str, input_type: type) -> any:
    """
    Parses input from the user.

    Parameters:
    ----------
    prompt : str
        The prompt to display to the user.
    input_type : type
        The type to convert the input to.

    Returns:
    -------
    any
        The parsed input.

    Raises:
    ------
    ValueError
        If the input is not valid.
    """
    while True:
        try:
            return input_type(input(prompt).strip())
        except ValueError:
            print(f"Invalid input! Please enter a valid {input_type.__name__}.")


def interface():
    """Runs the bank system interface."""
    bank = Bank()

    while True:
        print("\nWelcome to the Bank System!")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter account holder's name: ").strip()
            initial_deposit = parse_input("Enter initial deposit amount: ", float)
            try:
                bank.create_account(name, initial_deposit)
            except ValueError as e:
                print(e)

        elif choice == "2":
            account_number = parse_input("Enter account number to view: ", int)
            try:
                bank.view_account(account_number)
            except ValueError as e:
                print(e)

        elif choice == "3":
            account_number = parse_input("Enter account number to deposit into: ", int)
            amount = parse_input("Enter amount to deposit: ", float)
            try:
                bank.deposit(account_number, amount)
            except ValueError as e:
                print(e)

        elif choice == "4":
            account_number = parse_input("Enter account number to withdraw from: ", int)
            amount = parse_input("Enter amount to withdraw: ", float)
            try:
                bank.withdraw(account_number, amount)
            except ValueError as e:
                print(e)

        elif choice == "5":
            bank._save_to_file()
            print("All account data saved to file. Exiting.")
            break

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    interface()