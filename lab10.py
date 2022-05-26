import time
def fib_decorator(func):
    def wrapper():
        starttime=time.perf_counter()
        value=func()
        endtime = time.perf_counter()
        print(" start time is"+str(starttime))
        print("end time is "+str(endtime))

        runtime = endtime-starttime

        print("time taken=",runtime)
        return value
    return wrapper
@fib_decorator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
#        a=b
#       b=a+b
#dec1=fib_decorator(fib)

#dec1()
f=fib()
n=int(input('Enter value for Number:'))
for i in range(n):
    print(next(f))