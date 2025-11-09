class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

if __name__ == "__main__":
    account = BankAccount()
    while True:
        action = input("Choose action (deposit/withdraw/balance/exit): ").strip().lower()
        if action == "deposit":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif action == "withdraw":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif action == "balance":
            account.get_balance()
        elif action == "exit":
            break
        else:
            print("Invalid action. Please choose deposit, withdraw, balance, or exit.")
# ...existing code...