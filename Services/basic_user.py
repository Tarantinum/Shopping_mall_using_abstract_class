from Models.response import Response
from Services.Common.User import User


class BasicUser(User):

    def __init__(self, name, email, balance, date_of_membership):
        super().__init__(name, email, balance, date_of_membership)

    # by pressing alt+enter, you can get a suggestion for this implementation instead of copy and paste the code
    def withdraw(self, amount):
        if amount <= 0:
            return Response(False, "Invalid withdrawal amount", None)
        if self.balance < amount:
            return Response(False, "Insufficient balance", None)
        self.balance -= amount
        return Response(True, "Withdrawal successful", self.balance)

    def deposit(self, amount):
        if amount <= 0:
            return Response(False, "Invalid deposit amount", None)

        self.balance += amount
        return Response(True, "Deposit successful.",
                        {"balance": self.balance})

    def show_account_info(self):
        account_info = {
            "name": self.name,
            "email": self.email,
            "balance": self.balance,
            "membership_date": self.date_of_membership,
            "account_type": "Basic",

        }
        return Response(True, "Account information retrieved successfully", account_info)
