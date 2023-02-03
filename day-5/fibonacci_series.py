#fibonacci series using control statements and loops
n=int(input("enter your number:"))
a=0
b=1
sum=0
count=1
while(count<=n):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b
