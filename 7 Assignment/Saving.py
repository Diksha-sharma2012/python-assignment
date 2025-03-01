from Account import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, name, initial_balance, pin):
        super().__init__(name, initial_balance, 'Savings', pin)

    def withdraw(self, amount):
        if self.transaction_count >= 5:
            print("Transaction limit exceeded. A fee of 10 Rs will be charged for this transaction.")
            self.balance -= 10 
        if amount % 100 != 0:
            print("Withdrawal amount should be a multiple of 100.")
        elif amount > 10000:
            print("Maximum withdrawal limit is 10,000.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transaction_count += 1
            self.add_log('Withdrawal', amount)
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
