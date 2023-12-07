# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:39:48 2023

@author: deji
"""

class Account:
    all_account_numbers = []
    initial_account_number = 10001
    
    def __init__(self,FirstName, LastName, Age, nextofkin_name, Address, Network):
        if Account.initial_account_number not in Account.all_account_numbers:
            self.Account_number = Account.initial_account_number
            Account.all_account_numbers.append(self.Account_number)
        else:
            Account.initial_account_number +=1
            self.Account_number = Account.initial_account_number
            Account.all_account_numbers.append(self.Account_number)
        self.__Account_balance = 0.00
        self.__BVN = None
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__Age = Age
        self.__Nextofkin = nextofkin_name
        self.__Address = Address
        self.__Network = Network
        
    def deposit(self,amount):
        self.deposit_amount = float(amount)
        self.__Account_balance += self.deposit_amount
        
    def withdraw(self, with_amount):
        self.withdraw_amount = with_amount
        if self.withdraw_amount < 0:
            print("You cannot withdraw a negative amount")
        elif self.withdraw_amount == 0:
            print("Invalid Amount. You can only withdraw amounts greater than zero")
        elif self.__Account_balance >= with_amount:
            self.__Account_balance -= self.withdraw_amount
            
    def balance(self):
        return self.__Account_balance
    

    def new_account_number(self):
        return self.__Account_number

busola = Account("busola", "olonade", 25, "ade", "ajao estate", "MTN")

busola.deposit(300.00)
busola.withdraw(5)
print(busola.balance())

        
    
        

        
        