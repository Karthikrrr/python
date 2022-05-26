try:
    n=int(input("enter age"))
except Exception as e:
    print(e)

try:
    name=str(input("enter name "))
except Exception as e:
    print("enter string"+e)