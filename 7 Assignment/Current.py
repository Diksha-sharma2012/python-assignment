from Account import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, name, initial_balance, pin):
        super().__init__(name, initial_balance, 'Current', pin)

    def withdraw(self, amount):
        if amount % 100 != 0:
            print("Withdrawal amount should be a multiple of 100.")
        elif amount > 20000:
            print("Maximum withdrawal limit is 20,000.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transaction_count += 1
            self.add_log('Withdrawal', amount)
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
