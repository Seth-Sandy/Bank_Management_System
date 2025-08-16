from customer import *
from bank import Bank
import random

def signUp():
    username = input("Create username: ")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        print("Username already exists")
        signUp()
    else:
        print("Creating new user")
        password = input("Enter your password: ")
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        city = input("Enter your city: ")
        while True:
            account_number = random.randint(10000000, 99999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("New Account Created\nYour account number is: ",account_number)
                break
    cobj = Customer(username,password, name, age, city, account_number)
    cobj.createUser()
    bankobj = Bank(username,account_number)
    bankobj.create_transaction_table()

def signIn():
    username = input("Enter your username: ")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()}!\nEnter your password: ")
            temp = db_query(f"SELECT password FROM customers WHERE username = '{username}';")
            #print(temp[0][0])
            if temp[0][0] == password:
                print("Signed In successfully")
                return username
            else:
                print("Incorrect password. Try again")
                continue
    else:
        print("Username does not exist")
        signIn()
