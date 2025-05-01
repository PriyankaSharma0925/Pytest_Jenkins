
class BankDetails(object):
    def __init__(self,balance=0 ):
        self.balance=balance

    def deposit(self,balance):
        if self.balance<0:\
            raise ValueError('Balance cannot be negative')
        self.balance+=balance

    def get_balance(self):
        return self.balance

    def withdraw(self,sub_balance):
        if sub_balance> self.balance:
            raise ValueError("Sub balance cannot be greater than balance")
        self.balance-=sub_balance



