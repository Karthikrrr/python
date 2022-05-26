class Employee:
    raise_amt=1.04
    def _init_(self,first,last,empid,pay):
        self.first=first
        self.last=last
        self.empid=empid
        self.pay=pay
    def apply_raise(self,raise_amt):
        self.pay=self.pay*self.raise_amt
    def display(self):
        print("First Name:",self.first)
        print("Last Name:",self.last)
        print("Employee ID:",self.empid)
        print("Pay:",self.pay)
class Developer(Employee):
    def apply_raise(self,raise_amt):
        self.pay = self.pay * self.raise_amt
class Manager(Employee):
    def apply_raise(self,raise_amt):
        self.pay = self.pay * self.raise_amt

man={}
dev={}
n=int(input("Enter Number of Employee:"))
for i in range(1,n+1):
    print("1.Enter Manager Data:")
    print("2.Enter Developer Data:")
    print("3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        id=input("Enter employee ID:")
        first=input("Enter First Name:")
        last=input("Enter last Name:")
        raise_amt=int(input("Enter Raise amount:"))
        pay=int(input("Enter Pay Amount:"))
        e1=Employee(first,last,id,pay)
        e1.apply_raise(raise_amt)
        man[i]=e1._dict_
    elif ch==2:
        id = input("Enter employee ID:")
        first = input("Enter First Name:")
        last = input("Enter last Name:")
        raise_amt=int(input("Enter Raise amount:"))
        pay = int(input("Enter Pay Amount:"))
        e2 = Employee(first, last, id, pay)
        e2.apply_raise(raise_amt)
        man[i] = e2._dict_
    elif ch==3:
        break
    else:
        print("Invalid Input please try again")

print(man)
print(dev)