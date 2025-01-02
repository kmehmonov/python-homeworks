import json

class Account:
    """
    Represents a bank account.

    Attributes:
        account_number (int): The unique identifier for the account.
        name (str): The name associated with the account holder.
        balance (float | int): The balance in the account.

    Methods:
        to_dict: Converts the account data to a dictionary format for saving to a file.
        from_dict: Class method to create an Account instance from a dictionary.
    """
    def __init__(self, account_number: int, name: str, balance: float | int = 0) -> None:
        """
        Initializes a new bank account.

        Args:
            account_number (int): Unique identifier for the account.
            name (str): Account holder's name.
            balance (float | int): Initial balance (default is 0).
        """
        self.account_number = account_number
        self.name = name.capitalize()
        self.balance = balance

    def __str__(self):
        """
        Returns a string representation of the Account instance.
        """
        return f"Account({self.account_number}, {self.name}, {self.balance})"
    
    def to_dict(self) -> dict:
        """
        Converts the account instance to a dictionary.

        Returns:
            dict: A dictionary representation of the account.
        """
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }
    
    @classmethod
    def from_dict(cls, data) -> "Account":
        """
        Creates an Account instance from a dictionary.

        Args:
            data (dict): The dictionary containing account data.

        Returns:
            Account: A new Account instance.
        """
        return cls(data["account_number"], data["name"], data["balance"])

class Bank:
    """
    Represents a bank managing multiple accounts.

    Attributes:
        filename (str): The name of the file used for saving and loading account data.
        accounts (dict): A dictionary storing Account instances, keyed by account number.

    Methods:
        create_account: Creates a new account with a unique account number.
        view_account: Displays the details of an account.
        deposit: Deposits money into an account.
        withdraw: Withdraws money from an account.
        load_from_file: Loads account data from a file.
        save_to_file: Saves account data to a file.
        is_account_exist: Checks if an account exists by account number. If exist, it returns Account
    """
    filename = r"lesson-8/homework/accounts.txt"
    
    def __init__(self):
        """
        Initializes the Bank and loads account data from a file, if available.
        """
        self.accounts = self.load_from_file()

    def create_account(self, name: str, initial_deposit: float | int) -> None:
        """
        Creates a new bank account with a unique account number.

        Args:
            name (str): The name of the account holder.
            initial_deposit (float | int): The initial deposit for the account.

        Returns:
            Account: The newly created Account instance.
        """
        # Generate a unique account number
        if self.accounts:
            account_number = max(self.accounts.keys()) + 1  # Next available account number
        else:
            account_number = 1000  # Start with account number 1000 if no accounts exist

        # Create and store the new account
        self.accounts[account_number] = Account(account_number, name, initial_deposit)

    def view_account(self, account_number: int) -> None:
        """
        Displays the details of an account by account number.

        Args:
            account_number (int): The account number to view.

        Raises:
            ValueError: If the account does not exist.
        """
        try:
            account = self.is_account_exist(account_number)
            print(account)
        except ValueError as e:
            print(e)

    def deposit(self, account_number: int, amount: int | float) -> None:
        """
        Deposits a specified amount of money into an account.

        Args:
            account_number (int): The account number to deposit into.
            amount (float | int): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is not positive.
        """
        try:
            account = self.is_account_exist(account_number)
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            account.balance += amount
        except ValueError as e:
            print(e)

    def withdraw(self, account_number: int, amount: int | float):
        """
        Withdraws a specified amount of money from an account.

        Args:
            account_number (int): The account number to withdraw from.
            amount (float | int): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount exceeds the account balance or is invalid.
        """
        try:
            account = self.is_account_exist(account_number)
            if amount > account.balance:
                raise ValueError("Insufficient funds.")
            account.balance -= amount
        except ValueError as e:
            print(e)

    def load_from_file(self):
        """
        Loads account data from a file.

        Returns:
            dict: A dictionary of Account instances keyed by account number.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                # Convert loaded data into Account instances
                return {account_data["account_number"]: Account.from_dict(account_data) for account_data in data.values()}
        except (FileNotFoundError, json.JSONDecodeError):
            print("No previous data found, starting fresh.")
            return {}

    def save_to_file(self):
        """
        Saves all account data to a file in JSON format.
        """
        with open(self.filename, "w") as f:
            # Convert Account instances to dictionaries before saving
            json.dump({account_number: account.to_dict() for account_number, account in self.accounts.items()}, f, indent=4)

    def is_account_exist(self, account_number: int) -> Account:
        """
        Checks if an account exists in the bank by its account number.

        Args:
            account_number (int): The account number to check.

        Returns:
            Account: The Account instance if it exists.

        Raises:
            ValueError: If the account number does not exist.
        """
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number]


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Bank System!")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Save and Exit")
        
        try:
            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                name = input("Enter account holder's name: ").strip()
                initial_deposit = float(input("Enter initial deposit amount: ").strip())
                bank.create_account(name, initial_deposit)

            elif choice == "2":
                account_number = int(input("Enter account number to view: ").strip())
                bank.view_account(account_number)

            elif choice == "3":
                account_number = int(input("Enter account number to deposit into: ").strip())
                amount = float(input("Enter amount to deposit: ").strip())
                bank.deposit(account_number, amount)

            elif choice == "4":
                account_number = int(input("Enter account number to withdraw from: ").strip())
                amount = float(input("Enter amount to withdraw: ").strip())
                bank.withdraw(account_number, amount)

            elif choice == "5":
                bank.save_to_file()
                print("All account data saved to file. Exiting.")
                break
            
            else:
                print("Invalid choice! Please choose a valid option.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()