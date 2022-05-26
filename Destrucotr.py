class student:
    def __init__(self):
        print("cretaed")
    
    def __del__(self):
        print("delete")
    
s=student()
del s
s=student()