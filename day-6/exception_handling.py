#exception handling
a=100
b=0
try:# your are telling this may have error
    print(a/b)
except Exception as e:
    print("you are not allowed to divide by zero",e)#this will print the error message
print("bye")#to check wheather your program goes till end or not
