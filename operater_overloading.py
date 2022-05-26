class ov:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,o):
        return self.a+o.a,self.b+o.b

ob1=ov(2,3)
ob2=ov(1,2)
ob3=ob1+ob2
print(ob3)