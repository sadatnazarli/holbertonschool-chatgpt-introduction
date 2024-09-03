class Checkbook:
    """
    A class to represent a simple checkbook.

    Function Description:
    This class allows you to deposit, withdraw, and check the balance of an account.
    It provides basic functionality to manage and track the balance of a checkbook.

    Attributes:
    balance (float): The current balance of the checkbook, initialized to 0.0.
    """

    def __init__(self):
        """
        Initialize the Checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
        amount (float): The amount to be deposited.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook.

        Parameters:
        amount (float): The amount to be withdrawn.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the checkbook.

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook.

    Provides options to deposit, withdraw, check the balance, or exit the program.
    Includes error handling for invalid inputs.

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

