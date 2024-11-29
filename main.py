#Question : We will create a simple account system for online store customers.
# Each account includes information such as name, email, balance, and membership date.
# It should also be able to withdraw and deposit money from the account and display account information if the account is premium.
# With each deposit, one point is added to the user account.
# This feature is not available for the Basic account


from Services.Common.User import User
from Services.basic_user import BasicUser
from Services.Premium_user import PremiumUser
from datetime import datetime

# Create users
premium_user = PremiumUser("Taranom", "Tari@gmail.com", 1000, datetime.now())
basic_user = BasicUser("Hesam", "Hes123@gmail.com", 500, datetime.now())

# Test Premium User operations
print("=== Premium User Operations ===")
print("\nInitial Account Info:")
print(premium_user.show_account_info().data)

print("\nDepositing $200:")
deposit_result = premium_user.deposit(200)
print(deposit_result.message)
print(f"New balance: ${deposit_result.data['balance']}")
print(f"Points: {deposit_result.data['points']}")

print("\nWithdrawing $500:")
withdraw_result = premium_user.withdraw(500)
print(withdraw_result.message)
print(f"New balance: ${withdraw_result.data}")

print("\nFinal Premium Account Info:")
print(premium_user.show_account_info().data)

# Test Basic User operations
print("\n=== Basic User Operations ===")
print("\nInitial Account Info:")
print(basic_user.show_account_info().data)

print("\nDepositing $150:")
deposit_result = basic_user.deposit(150)
print(deposit_result.message)
print(f"New balance: ${deposit_result.data}")

print("\nWithdrawing $300:")
withdraw_result = basic_user.withdraw(300)
print(withdraw_result.message)
print(f"New balance: ${withdraw_result.data}")

print("\nFinal Basic Account Info:")
print(basic_user.show_account_info().data)
