# create an abstract class
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, email, balance, date_of_membership):
        self.name = name
        self.email = email
        self.balance = balance
        self.date_of_membership = date_of_membership

    @abstractmethod
    def withdraw(self,amount):
        pass  # abstract method doesn't have any implementation

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def show_account_info(self):
        pass
