import random
from datetime import datetime

# Main Menu
def main_menu():
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid choice. Please try again.")

# Create Account
def create_account():
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter your initial deposit: "))
    password = input("Enter a password: ")

    account_number = random.randint(100000, 999999)
    with open("accounts.txt", "a") as f:
        f.write(f"{account_number},{name},{password},{initial_deposit}\n")

    print(f"Account created successfully! Your account number is {account_number}. Save it for login.")

# Login
def login():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

    with open("accounts.txt", "r") as f:
        accounts = f.readlines()

    for account in accounts:
        acc_num, name, acc_password, balance = account.strip().split(',')
        if acc_num == account_number and acc_password == password:
            print(f"Login successful! Welcome, {name}.")
            user_menu(account_number)
            return

    print("Invalid account number or password.")

# User Menu
def user_menu(account_number):
    while True:
        print("\n1. View Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_balance(account_number)
        elif choice == '2':
            deposit(account_number)
        elif choice == '3':
            withdraw(account_number)
        elif choice == '4':
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice. Please try again.")

# View Balance
def view_balance(account_number):
    with open("accounts.txt", "r") as f:
        accounts = f.readlines()

    for account in accounts:
        acc_num, name, password, balance = account.strip().split(',')
        if acc_num == account_number:
            print(f"Your current balance is: ₹{balance}")
            return

# Deposit
def deposit(account_number):
    amount = float(input("Enter amount to deposit: ₹"))
    if update_balance(account_number, amount):
        log_transaction(account_number, "Deposit", amount)
        print("Deposit successful!")
    else:
        print("Error during deposit.")

# Withdraw
def withdraw(account_number):
    amount = float(input("Enter amount to withdraw: ₹"))
    if update_balance(account_number, -amount):
        log_transaction(account_number, "Withdrawal", amount)
        print("Withdrawal successful!")
    else:
        print("Insufficient balance.")

# Update Balance
def update_balance(account_number, amount):
    updated = False
    accounts = []

    with open("accounts.txt", "r") as f:
        accounts = f.readlines()

    with open("accounts.txt", "w") as f:
        for account in accounts:
            acc_num, name, password, balance = account.strip().split(',')
            if acc_num == account_number:
                new_balance = float(balance) + amount
                if new_balance < 0:
                    return False
                f.write(f"{acc_num},{name},{password},{new_balance}\n")
                updated = True
            else:
                f.write(account)

    return updated

# Log Transaction
def log_transaction(account_number, transaction_type, amount):
    date = datetime.now().strftime("%Y-%m-%d")
    with open("transactions.txt", "a") as f:
        f.write(f"{account_number},{transaction_type},{amount},{date}\n")

# Start the Program
if __name__ == "__main__":
    main_menu()
