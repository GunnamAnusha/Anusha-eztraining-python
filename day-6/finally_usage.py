#exception handling
a=100
b=0
try:# your are telling this may have error
    print(a/b)
except Exception as e:
    print("you are not allowed to divide by zero",e)#this will print the error message
finally:
  print("resource closed")#always executed if therev is error or not
