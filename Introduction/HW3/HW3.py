from functools import reduce
import datetime
from types import FunctionType


#Q1
def sum_list(lst):
    return reduce((lambda x, y: x + y), lst)


#q1
list1 = [1, 2, 3, 4]
print(sum_list(list1))


#Q2
def goto():
    while True:
        num = int(input())
        if num < 0:
            break
        if num % 2 == 0:
            print("even")
        else:
            print("odd")
    print("all done")


# #q2
goto()

#Q3
#3b
def get_date(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(datetime.datetime.now())
    return inner


#3a
class Account(object):
    def __init__(self, name, acc_num, balance: float):
        self._name = name
        self._acc_num = acc_num
        self._balance = balance
        self._credit = 1500

    @get_date
    def withdraw(self, to_withdraw: float):
        if self._balance >= to_withdraw:
            self._balance = self._balance - to_withdraw

    @get_date
    def deposit(self, to_deposit: float):
        self._balance = self._balance + to_deposit

    def get_balance(self):
        return self._balance

    def transfer(self, receiver, amount: float):
        self._balance = self._balance - amount
        receiver._balance = receiver._balance + amount
        return receiver


#3c
def account_generator(account_list):
    count = 0
    for j in account_list:
        count = count + j.get_balance()
    yield count


account1 = Account("lir1", 1234, 100)
account2 = Account("lir2", 1234, 200)
account3 = Account("lir3", 1234, 300)
list_of_accounts = [account1, account2, account3]
for i in account_generator(list_of_accounts):
    print(i)


#Q4
def functions(cls):
    return [x for x, y in cls.__dict__.items() if type(y) == FunctionType if '__' not in x]


list_method_in_Account = functions(Account)
print("account1", getattr(account1, list_method_in_Account[2])())
getattr(account1, list_method_in_Account[0])(80)
print("account1", getattr(account1, list_method_in_Account[2])())
getattr(account1, list_method_in_Account[1])(80)
print("account1", getattr(account1, list_method_in_Account[2])())
getattr(account1, list_method_in_Account[3])(account2, 120)
print("account1", getattr(account1, list_method_in_Account[2])())
print("account2", getattr(account2, list_method_in_Account[2])())
getattr(account2, list_method_in_Account[3])(account3, 100)
print("account2", getattr(account2, list_method_in_Account[2])())
print("account3", getattr(account3, list_method_in_Account[2])(), "\n")


#Q5
def words_generator(word_list):
    for j in word_list:
        if "e" not in j:
            yield j


file = open("words.txt", "r")
list_word = file.read().split(",")
for i in words_generator(list_word):
    print(i)

