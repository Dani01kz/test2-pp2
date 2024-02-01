class KaspiBank:
    def __init__(self,owner,balance):
        self.own=owner
        self.blnc=balance
        print(f"{self.own} your balanace :{self.blnc}")
    def deposit(self,money):
        if(money>=0):
           self.blnc+=money
           print(f"{self.own} your balanace :{self.blnc}")
        else:
            print("Error:\"You cannot deposit a negative amount of money\"")
    def withdraw(self,_minus_m):
        if(self.blnc>=_minus_m):
            self.blnc-=_minus_m
            print(f"{self.own} your balanace :{self.blnc}")
        else:
            print("Error:\"You don't have enough money to write off\"")
Dani=KaspiBank("Dani",2000)
Dani.deposit(200000)

Dani.withdraw(50000)

Dani.withdraw(1000000)
