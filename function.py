import datetime

def currenttime():
    x = datetime.datetime.now()
    print(x)
    print(x.strftime("%B"))
    print(x.strftime("%b"))
    print(x.strftime("%w"))
    print(x.strftime("%A"))

currenttime()