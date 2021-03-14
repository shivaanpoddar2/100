class ATM(object):
    def __init__(self,BankName):
        self.BankName = BankName
        self.Balance = 500
    def withdraw(self):
        print("witdrawing")

    def deposit(self):
        print("depositing")

    def transanctions(self):
        print("Showing transanctions")
    
    def Balance(self,gear):
        print("Balance of this stupid poor man " + str (self.Balance))

americanexpress = ATM("stupid banks")
print (americanexpress.BankName)
americanexpress.withdraw()
americanexpress.deposit()