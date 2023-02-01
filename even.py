n=int(input("enter  a number"))
if(n%2==0 and n>0):
    print("number is even-positive")
elif(n%2!=0 and n>0):
    print("number is odd-positive")
elif(n%2==0 and n<0):
    print("number is even negative")
elif(n%2!=0 and n<0):
    print("number is odd-negative")
else:
    print("not a valid number")
