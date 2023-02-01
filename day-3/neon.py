n=int(input("enter a number:"))
sqr=n**2
sum=0
while sqr>0:
    digit=sqr%10
    sum=sum+digit
    sqr=sqr//10
if (sum==n):
    print("it is a neon number:",n)
else:
    print("not a neon number:",n)
