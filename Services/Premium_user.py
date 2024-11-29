from Models.response import Response
from Services.Common.User import User


class PremiumUser(User):

    def __init__(self, name, email, balance, date_of_membership):
        super().__init__(name, email, balance, date_of_membership)
        self.points = 0

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
        self.points += 1
        return Response(True, "Deposit successful. You have Earned one point!",
                        {"balance": self.balance, "points": self.points})

    def show_account_info(self):
        account_info = {
            "name": self.name,
            "email": self.email,
            "balance": self.balance,
            "membership_date": self.date_of_membership,
            "account_type": "Premium",
            "points": self.points
        }
        return Response(True, "Account information retrieved successfully", account_info)
