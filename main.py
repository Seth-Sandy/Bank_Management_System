from register import *
from bank import *

status = False
print("Welcome to My Bank Management System Project")
while True:
    try:
        register = int(input("1. SignUp\n2. Login\n3. Exit\n"))
        if register == 1 or register == 2:
            if register == 1:
                signUp()
            elif register == 2:
                user = signIn()
                status = True
                break
        elif register == 3:
            exit()
        else:
            print("Please enter a valid choice number.")

    except ValueError:
        print("Please enter a valid number input.")

account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")
#print(account_number[0][0])

print(f"\nWelcome {user.capitalize()}!")
while status:
    try:
        print("\nChoose your Banking Service")
        facility = int(input("1. Balance Enquiry\n2. Cash Deposit\n3. Cash Withdraw\n4. Fund Transfer\n5. Exit\n"))
        if facility >= 1 or facility <= 5:
            if facility == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.balanceEnquiry()
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter amount to deposit: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter amount to withdraw: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter the Account Number you wish to transfer funds: "))
                        amount = int(input("Enter amount to transfer: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundTransfer(receive, amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Please enter a valid Account Number.")
                        continue
            elif facility == 5:
                exit()
        else:
            print("Please enter a valid number.")
            continue
    except ValueError:
        print("Please enter a valid number.")
