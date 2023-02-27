n=int(input("enter the num:"))
while(n>=10):
    s=0
    for i in range(0,len(str(n))+1):
        r=n%10
        s=s+r**2
        n=n//10
    n=s
if n==1:
    print("happy number")
else:
    print("not a happy number")
 
