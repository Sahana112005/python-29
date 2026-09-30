#accessing class attributes

class mike:
    clr="Blue"
    lng=6
    shape="cylindrical"
m=mike()
print(m.clr)
print(m.lng)
print(m.shape)





#we can create same class two object

class mike:
    clr="Blue"
    lng=6
    shape="cylindrical"
m=mike()
print(m.clr)
print(m.lng)
print(m.shape)
m2=mike()
print(m2.clr)





class mike:
    clr="Blue"
    lng=6
    shape="cylindrical"
    def func(m):
        print("receving voice")
m=mike()
print(m.clr)
print(m.lng)
print(m.shape)
m.func()
m2=mike()
m2.func()

#addition


class sum:               #class
    a=5
    b=5
    def add():            #func
        c=a+b
        print(c)
addition=sum             #obj
print(addition.a+addition.b)


#new mike with new values
#single
class mike:
    cmpi="SVIST"
    def mike(self,clr,len,shape):
        self.clr=clr
        self.len=len
        self.shape=shape
    def show(self):
        print(self.clr,self.len,self.shape)
m=mike()
m.mike("white",6,"cylindrical")
m.show()

#double
class mike:
    cmpi="SVIST"
    def mike(self,clr,len,shape):
        self.clr=clr
        self.len=len
        self.shape=shape
    def show(self):
        print(self.clr,self.len,self.shape)
m=mike()
m.mike("white",6,"cylindrical")
m.show()
m2=mike()
m2.mike("black",7,"square")
m2.show()
m3=mike()
m3.mike("red",8,"rectangle")
m3.show()




#constructor



class mike:
    cmpi="SVIST"
    def __init__(self,clr,len,shape):
        self.clr=clr
        self.len=len
        self.shape=shape
    def show(self):
        print(self.clr,self.len,self.shape)

m1=mike("white",6,"cylindrical")
m1.show()
m2=mike("black",7,"square")
m2.show()
m3=mike("red",8,"rectangle")
m3.show()
print(m1.cmpi)




class bankaccount:
    bname="SBI"
    def __init__(self,username,accno,ifsc,balance):

          self.username=username
          self.accno=accno
          self.ifsc=ifsc
          self.balance=balance

    def acc(self):

          print("username:",self.username)
          print("accno:",self.accno)
          print("ifsc:",self.ifsc)
          print("balance:",self.balance)
b1=bankaccount("sahana",2323434545,"34325465346",54666)
b1.acc()  
b2=bankaccount("srii",2333434545,"33345465346",5666)
b2.acc() 






#adding money to bank  acc to paticular user
#deposit


class bankaccount:
    bname="SBI"
    def __init__(self,username,accno,ifsc,balance):

          self.username=username
          self.accno=accno
          self.ifsc=ifsc
          self.balance=balance
    def deposit(self,amount):
        self.amount=amount
        if self.amount>0:
            self.balance=self.balance+self.amount
            print("amount deposited successfully")
        print(self.balance)    

    def acc(self):

          print("username:",self.username)
          print("accno:",self.accno)
          print("ifsc:",self.ifsc)
          print("balance:",self.balance)
b1=bankaccount("sahana",2323434545,"34325465346",400000)
b1.deposit(10000)
b1.deposit(-10000)
b2=bankaccount("srii",2453426356563,"135315255",50000)
b2.deposit(10000)














#withdraw

class bankaccount:
    bname="SBI"
    def __init__(self,username,accno,ifsc,balance):

          self.username=username
          self.accno=accno
          self.ifsc=ifsc
          self.balance=balance
    def deposit(self,amount):
        self.amount=amount
        if self.amount>0:
            self.balance=self.balance+self.amount
            print("amount deposited successfully")
        print(self.balance)

    def withdraw(self,amount):
        self.amount=amount
        if self.amount>0:
            self.balance=self.balance-self.amount
            print("amount withdraw successfully")
        print(self.balance)    

    def acc(self):

          print("username:",self.username)
          print("accno:",self.accno)
          print("ifsc:",self.ifsc)
          print("balance:",self.balance)
b1=bankaccount("sahana",2323434545,"34325465346",400000)
b1.deposit(10000)
b1.deposit(-10000)
b2=bankaccount("srii",2453426356563,"135315255",50000)
b2.deposit(10000)
b1.withdraw(500)




#amount more than given


class bankaccount:
    bname="SBI"
    def __init__(self,username,accno,ifsc,balance):

          self.username=username
          self.accno=accno
          self.ifsc=ifsc
          self.balance=balance
    def deposit(self,amount):
        self.amount=amount
        if self.amount>=0:
            self.balance=self.balance+self.amount
            print("amount deposited successfully")
        print("total balance:",self.balance)

    def withdraw(self,amount):
        self.amount=amount
        if self.amount<self.balance:
            self.balance=self.balance-self.amount
            print("amount withdraw successfully")
        else:
            print("insufficent balance")
        print("Available balance:",self.balance)    

    def acc(self):

          print("username:",self.username)
          print("accno:",self.accno)
          print("ifsc:",self.ifsc)
          print("balance:",self.balance)
b1=bankaccount("sahana",2323434545,"34325465346",400000)
b1.deposit(10000)
b1.deposit(-10000)
b2=bankaccount("srii",2453426356563,"135315255",50000)
b2.deposit(10000)
b1.withdraw(1000000000000)

#inheritance
#single inheritance

class person:
    def eating(self):
        print("eating")
    def sleep(self):
        print("sleeping")
    def walk(self):
        print("walking")
class student(person):
    def read(self):
        print("reading")
s=student()
s.read()
s.walk()
s.eating()


#multilevel

class person:
    def eating(self):
        print("eating")
    def sleep(self):
        print("sleeping")
    def walk(self):
        print("walking")
class student(person):
    def read(self):
        print("reading")
s=student()
s.read()
s.walk()
s.eating()
class professional(student):
    def work(self):
        print("working")
    def login(self):
        print("login in time")
    def salary(self):
        print("salary credited")
p=professional()
p.work()
    









































































