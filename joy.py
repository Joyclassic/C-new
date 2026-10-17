class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_num =acc
    def debit(self,ammount):
        self.balance-=ammount
        


