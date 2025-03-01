import random
import json
from abc import abstractmethod 

class BankAccount:
    account_details = []
    
    bank_name = "AMAN POISION BANK"
    
    def __init__(self, name, initial_balance, account_type, pin):
        self.account_number = random.randint(100000, 999999)  
        self.name = name
        self.balance = initial_balance
        self.account_type = account_type
        self.min_balance = 0 
        self.transaction_count = 0
        self.transaction_log = {} 
        self.pin = pin 
        print('*'*66)
        print("       Welcome!", self.name, "to", self.bank_name)
        print('*'*66)
        
        
    def add_log(self, transaction_type, amount):
        transaction_id = len(self.transaction_log) + 1
        self.transaction_log[transaction_id] = {
            'transaction_type': transaction_type,
            'amount': amount,
            'balance_after': self.balance
        }    
      
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_count += 1
            self.add_log('Deposit', amount)
            print(f"Deposit successful. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than 0.")
            
    @abstractmethod        
    def withdraw(self):
        pass        
            
            
    def account_info(self):
        print(f"Account Information for {self.name}:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance}")  
        
        
    def balance_enquiry(self):
        print(f"Balance Enquiry: {self.balance}") 
        
    def validate_pin(self, pin_attempt):
        return pin_attempt == self.pin 
    
    
    
    def store_account_info(self, file_path):
        try:
            data = {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
            "account_type": self.account_type,
            "min_balance": self.min_balance,
            "transaction_count": self.transaction_count,
            "transaction_log": self.transaction_log,
            "pin": self.pin
        }
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)  
                print(f"Account data for {file_path} has been stored successfully!")
        except Exception as e:
            print(f"An error occurred while storing account info: {e}")   

    
# with open("employee_data.json","w",encoding="utf-8") as file:
#    for text in account_details:
#       file.write(json.dumps(text,indent=4))




    # def store_account_info(self, file_path):
    #     try:
    #         account_info = self.to_dict()  
    #         with open(file_path, 'w') as file:
    #             json.dump(account_info, file, indent=4)  
    #             print(f"Account data for {self.name} has been stored successfully!")
    #     except Exception as e:
    #         print(f"An error occurred while storing account info: {e}")
            
    # # store_account_info()

                 

    