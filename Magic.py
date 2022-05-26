class magic:
    def __init__(self,a):
        self.a=a
        #self.other
    def __add__(self,other):
        print(self.a+other.a)

c=magic(1123)
c1=magic(12)
print(c+c1)
