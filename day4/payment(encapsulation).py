# with encapsulation
class Payment:
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        print("amount")

class CashPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print(f'Paid Rs.{self.amount} in cash')

class CardPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print(f'Paid Rs.{self.amount} using credit/debit card')

class UPIPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print(f'Paid Rs.{self.amount} using UPI')     

l=[CashPayment(1000),CardPayment(1000),UPIPayment(1000)]
for i in l:
    i.pay()   


# without encapsulation
class Payment:
    def pay(self, amount):
        print("amount")


class CashPayment(Payment):
    def pay(self, amount):
        print(f'Paid Rs.{amount} in cash')


class CardPayment(Payment):
    def pay(self, amount):
        print(f'Paid Rs.{amount} using credit/debit card')


class UPIPayment(Payment):
    def pay(self, amount):
        print(f'Paid Rs.{amount} using UPI')



l = [CashPayment(), CardPayment(), UPIPayment()]


for i in l:
    i.pay(1000)
