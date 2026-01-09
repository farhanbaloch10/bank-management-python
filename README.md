# bank-management-python
🏦 Bank Management System
A lightweight and easy-to-use application designed to automate basic banking operations.
✨ Key Features
Account Management: Create, view, and delete customer accounts.
Transactions: Easy deposit and withdrawal system.
Balance Check: Quick inquiry of current account balance.
Data Storage: Saves all records to a [File/Database] for future use.
🛠️ Tech Stack
Language: [Insert Language, e.g., Python or C++]
Storage: [Insert Storage, e.g., Text Files or SQL]
🚀 How to Run
Download or clone the repository.
Open the project in your IDE.
Run the main file to start the system.
Bank Account Management System in Python
[!https://img.shields.io/badge/Python-3.x-blue.svg](https://www.python.org/)
[!https://img.shields.io/badge/License-MIT-green.svg](https://opensource.org/licenses/MIT)

A simple and intuitive bank account management system implemented in Python, demonstrating key object-oriented programming (OOP) concepts like encapsulation, inheritance, and polymorphism.

Features- Create and manage bank accounts with basic operations like deposit, withdrawal, and balance check
- Implement savings and current accounts with specialized features like interest rates and overdraft limits
- Transfer funds between accounts seamlessly
- Easy-to-use command-line interface

Code Structure- account.py: Defines the Account class with basic operations
- savings_account.py: Defines the SavingsAccount class with interest rate feature
- current_account.py: Defines the CurrentAccount class with overdraft limit feature
- bank_manager.py: Defines the BankManager class for managing accounts and transfers
- main.py: The main program that demonstrates the usage of the classes

Getting Started1. Clone the repository: git clone https://github.com/farhanalmani/bank-account-management.git
2. Navigate to the project directory: cd bank-account-management
3. Run the program: python main.py

Usage1. Create an account: bank_manager.create_account("12345", 1000)
2. Deposit money: account.deposit(500)
3. Withdraw money: account.withdraw(200)
4. Check balance: account.get_balance()
5. Transfer funds: bank_manager.transfer("12345", "67890", 500)

ContributingFeel free to fork, modify, and submit pull requests to improve this project. Your contributions are highly appreciated!

LicenseThis project is licensed under the MIT License. See LICENSE for details.

Author- https://github.com/farhanalmani
