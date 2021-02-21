#exception1.py
try:
    #print (x)
    x = 5
    y = 1
    z = x /y
    print('x'+y)

except NameError as e:
    print(e)
except ZeroDivisionError:
    print("Division by 0 is not allowed")
except Exception as e:
    print("An error occured")
    print(e)
