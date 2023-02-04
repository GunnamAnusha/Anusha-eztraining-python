#like specialised doctors
#for those specific errors only those exception
#blocks will get executed
a=10
try:
    b=int(input("enter your second number:"))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("you are not allowed to divide by zero",e)
except ValueError as e:
    print("invalid input",e)
except Exception as e:#if not any above errors
    print("other error",e)
finally:
    print("resource closed")
