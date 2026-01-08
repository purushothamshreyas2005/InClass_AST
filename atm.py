print("Welcome To ATM Machine")
balance=int(input("Enter your account balance:"))
withdraw=int(input("Enter withdrawl amount"))
if withdraw%100!=0:
    print("Withdrawal amount must be a multiple of 100")
elif withdrawal>balance:
    print("Insufficient balance")
else:
    balance-=withdraw
    print("withdrawl successful")
    print("updated balance=",balance)