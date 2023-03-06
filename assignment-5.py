# Challenge 1: Square Numbers and Return Their Sum

class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def add(self,a,b,c):
        a = self.x**2
        b = self.y**2
        c = self.z**2
        return a,b,c
    
    def sqSum(self):
        square = self.x**2 + self.y**2 + self.z**2
        return square
num1=int(input('enter num1:'))
num2=int(input('enter num2:'))
num3=int(input('enter num3:'))

obj=Point(num1, num2, num3)
print(obj.sqSum())

#Challenge 2: Implement a Calculator Class
class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return(self.num2+self.num1)
    def subtract(self):
        return(self.num2-self.num1)
    def multiply(self):
        return(self.num2*self.num1)
    def divide(self):
        return(self.num2/self.num1)
num1=int(input('enter your num'))
num2=int(input('enter your num'))
demo1=Calculator(num1,num2)
print("Addition:", demo1.add())
print("Subtraction:", demo1.subtract())
print("Mutliplication:", demo1.multiply())
print("Division:", demo1.divide())

#Challenge 3: Implement the Complete Student Class
class student:

    def init(self,Name,Rollno):
        self._name=Name
        self._rollno=Rollno
    def set_name(self,x):
        self._name=x
        pass
    def get_name(self):
        return self._name
    pass
    def set_rollno(self,x):
        self._rollno=x
        pass
    def get_rollno(self):
        return self._rollno
    pass
name=input("enter name")
rollno=int(input("enter roll no"))
s=student()
s.set_name(name)
print(s.get_name())
#s.get_name()
s.set_rollno(rollno)
print(s.get_rollno())

#Challenge 4: Implement a Banking Account

 class Account:

    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
        

class SavingsAccount(Account):
    def __init__(self,title,balance,interestRate):
        self.title=title
        self.balance=balance
        self.interestRate = interestRate
    def display(self):
        return(f'{self.title}is the title, and the {self.balance} is the account balance, and {self.interestRate} is the interestRate')
name=input('enter your name')
bal=int(input('enter your balance'))
irt=int(input('enter your interestRate %'))
obj=SavingsAccount(name,bal,irt)
print(obj.display())

# Challenge 5: Handling a Bank Account
class user:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    def getbalance(self):
         return self.balance
    def deposite(self):
         amount = float(input('enter the amount to be deposited'))
         self.balance = self.balance + amount
         print('deposite is successful and the balance in the account is %f' % self.balance)
         

    def withdraw(self):
         amount = float(input('enter the amount to withdraw'))
         self.amount = amount
         if self.amount > self.balance:
              print('Insufficient Funds | Balance Available: Rs',self.balance)
         else:
              self.balance = self.balance - self.amount
              print('Account balance has been updated: Rs',self.balance)
    def enquiry(self):
         print('balance in the account is %f' % self.balance)
    
class SavingsAccount(user):
    def __init__(self, title, balance, interestRate):
          super().__init__(title, balance)
          self.interestRate = interestRate
    def interestAmount(self):
         return(self.interestRate*self.Balance)/100
name=input('Enter customer name: ')
balance=float(input('enter your amount'))
itr=float(input('interestRate'))
customer1 = SavingsAccount(name,balance,itr)
print(customer1.getbalance())
customer1.deposite()
print(customer1.getbalance())
customer1.withdraw()
print(customer1.getbalance())



    

