class hi:
    def hello(self):
        print("ok friend")


try :
    h=hi()
    h.hello()

except Exception as e:
    print(e)