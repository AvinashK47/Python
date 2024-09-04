class Bank :
    def __init__(self,AcNum,AcName, AcBal=0):
        self.AcNum=AcNum
        self.AcName=AcName
        self.AcBal=AcBal
    def Deposit(self,money):
        self.AcBal=self.AcBal+money
    def Withdraw(self,withdraw):
        if self.AcBal>withdraw:
            self.AcBal=self.AcBal-withdraw
    def display(self):
        print(self.AcBal,self.AcName,self.AcNum)
mybank=Bank(13423525,"Avinash")
mybank.display()
mybank.Deposit(3000)
mybank.display()
mybank.Withdraw(1000)
mybank.display()