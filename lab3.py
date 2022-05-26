
d=dict()
class employee():
    def add_emp(self):
        self.name=input("enetr name")
        self.address=input("enter address ")
        self.hra=input("enetr hra")
        self.salary=input("enter sal")
        self.update_emp()
    
    def update_emp(self):
        d.update({self.name:{"name is":self.name, "address ":self.address,"hra":self.hra,"salary":self.salary}})

    def search_emp(self,name):
        flag=0
        for key in d:
            if key==name:
                print("found")
                for i in d[key]:
                    print(i,d[key][i])
                    flag= 0
            if flag==0:
                print("not found")
        
    def print_emp(self):
        for key in d:
            print (key,d[key])

class operations (employee):
    em=employee()
    ch=input ("Enter choice")
    if(ch==1):
        print("oposd")
        em=employee()
        em.add_emp()
    elif(ch==2):
        name=input("enter name")
        em.search_emp(name)
    elif ch==3:
        em.print_emp()