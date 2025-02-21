class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    def debit(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
            print(f"Account No. {self.account_no} Debited: {amount} Rest: {self.balance}")
        else:
            print("Insufficient balance")
    def credit(self,amount):
        self.balance+=amount
        print(f"Account No. {self.account_no} Credited amount: {amount} New Balance: {self.balance}")
    def print_balance(self):
        print(f"Account {self.account_no} Current Bank Balance: {self.balance}")


account1=Account(0,2201006)
account2=Account(0,2201007)

account1.credit(1000)
account2.credit(500)

account1.debit(10)
account2.debit(330)


account1.print_balance()
account2.print_balance()
