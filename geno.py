# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.
# print("Hello world")
# import time

# def timeit(func):
#         def check(*args,**kw):
#                 starttime=time.time()
#                 result=func(*args,**kw)
#                 endtime=time.time()
#                 print("end is :",endtime)
#                 return result
#         return check

# @timeit
# def fib(a=0,b=1):
#         yield a
#         a,b=b,a+b

# f=fib()
# n=int(input("enter num"))
# for i in range(n):
#         print(next(f))
import time

def timeit(func):
        def check(*args,**kw):
                starttime=time.time()
                result=func(*args,**kw)
                endtime=time.time()
                print("end is :",starttime-endtime)
                return result
        return check

@timeit
def fib(a=0,b=1):
    while True:
        yield a
        a,b=b,a+b

f=fib()
n=int(input("enter num"))
for i in range(n):
        print(next(f))
