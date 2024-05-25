####################################
#Choiden Zangmo
#First Year Electrical Department
#02230061
####################################
#References
#Chatgpt
#youtube

import time #used to generate unique account numbers and passwords based on the current time
import os # (operating system) used to check if the file “accounts.txt” exists before trying to open it
import json # (JavaScript Object Notation)used to save and load account information to and from a file in JSON format

#Defining the BankAccount Class
class BankAccount:
    def __init__(self, account_type, balance=0):
        self.account_number = self.generate_account_number()
        self.password = self.generate_password()
        self.account_type = account_type
        self.balance = balance

  #Generating a unique account number
    def generate_account_number(self):
        return "211" + str(int(time.time() * 1000))[-6:]
 
  #Generating a default password
    def generate_password(self):
        return str(int(time.time() * 1000))[-4:]
 
 #To deposit money into the account 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully.")
        else:
            print("Deposit amount must be positive.")
 
 #To withdraw money from  the account
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn {amount} successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
 
 #To transfer money to another account
    def transfer(self, recipient, amount):
        if amount > 0:
            if self.balance >= amount:
                self.withdraw(amount)
                recipient.deposit(amount)
                print(f"Transferred {amount} to {recipient.account_number} successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Transfer amount must be positive.")
 
  # To delete the accoint
    def delete_account(self):
        return self.account_number

#To define the PersonalAccount class, which inherits from BankAccount
class PersonalAccount(BankAccount):
    def __init__(self, balance=0):
        super().__init__("Personal", balance)

#To define the BusinessAccount class, which inherits from BankAccount
class BusinessAccount(BankAccount):
    def __init__(self, balance=0):
        super().__init__("Business", balance)

#To define Main function to run the banking application
def main():
    accounts = []
     # Load existing accounts from file
    if os.path.exists("accounts.txt"):
        with open("accounts.txt", "r") as file:
            account_dicts = json.load(file)
            for account_dict in account_dicts:
                if account_dict["account_type"] == "Personal":
                    account = PersonalAccount()
                else:
                    account = BusinessAccount()
                account.account_number = account_dict["account_number"]
                account.password = account_dict["password"]
                account.balance = account_dict["balance"]
                accounts.append(account)

# Main loop for the banking application
    while True:
        print("\nWelcome to the Banking Application!")
        print("1. Open a new account")
        print("2. Login to your account")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
      
       # To open a new account
        if choice == "1":
            account_type = input("Enter account type (Personal/Business): ").lower()
            if account_type == "personal":
                account = PersonalAccount()
                accounts.append(account)
            elif account_type == "business":
                account = BusinessAccount()
                accounts.append(account)
            else:
                print("Invalid account type.")
                continue
            print(f"Your account number is: {account.account_number}")
            print(f"Your password is: {account.password}")
           # Save the new account to file
            with open("accounts.txt", "w") as file:
                json.dump([account.__dict__ for account in accounts], file)

         #To Login to an existing account
        elif choice == "2":
            account_number = input("Enter your account number: ")
            password = input("Enter your password: ")

            #To find the account in the list of accounts
            account = next((acc for acc in accounts if acc.account_number == account_number and acc.password == password), None)
            if account:
                while True:
                    print(f"\nWelcome, {account.account_type} account holder!")
                    print("1. Check balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. Delete account")
                    print("6. Logout")

                    choice = input("Enter your choice (1-6): ")
                     #To Check balance
                    if choice == "1":
                        print(f"Your balance is: {account.balance}")
                    #To Deposit money
                    elif choice == "2":
                        try:
                            amount = float(input("Enter the amount to deposit: "))
                            account.deposit(amount)
                        except ValueError:
                            print("Invalid amount. Please enter a numeric value.")
                    #To Withdraw money
                    elif choice == "3":
                        try:
                            amount = float(input("Enter the amount to withdraw: "))
                            account.withdraw(amount)
                        except ValueError:
                            print("Invalid amount. Please enter a numeric value.")
                    #To Transfer money
                    elif choice == "4":
                        recipient_number = input("Enter the recipient's account number: ")
                        recipient = next((acc for acc in accounts if acc.account_number == recipient_number), None)
                        if recipient:
                            try:
                                amount = float(input("Enter the amount to transfer: "))
                                account.transfer(recipient, amount)
                            except ValueError:
                                print("Invalid amount. Please enter a numeric value.")
                        else:
                            print("Recipient account not found.")
                    #To Delete account
                    elif choice == "5":
                        accounts.remove(account)
                        print("Account deleted successfully.")
                        with open("accounts.txt", "w") as file:
                            json.dump([account.__dict__ for account in accounts], file)
                        break
                    #To Logout
                    elif choice == "6":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid account number or password.")

        elif choice == "3":
            print("Exiting the Banking Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
