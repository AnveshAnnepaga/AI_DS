class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance #private variable
    def deposit(self,amount):
        if amount>0:
            self.__balance +=amount
        else:
            print(f'amount must be +ve')

    def get_balance(self):
        print(f'balance of my account:{self.__balance}')
    
    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance -=amount
        elif amount<=0:
            print(f'withdrawal amount must be +ve')
        else:
            print(f'Insuffient balance')

b = BankAccount()
b.deposit(int(input("Deposit:")))
b.get_balance()
b.withdraw(int(input("withdrawal:")))
b.get_balance()