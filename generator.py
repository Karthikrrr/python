def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
   
# x is a generator object
x = simpleGeneratorFun()
  
# Iterating over the generator object using next
print(x.next()) # In Python 3, __next__()
print(x.next())
print(x.next())