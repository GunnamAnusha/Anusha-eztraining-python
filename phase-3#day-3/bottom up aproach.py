def fib(n):
    if n==0 or n==1:
        return 1
    a=0
    b=1
    for i in range(2,n+1):
        temp=a+b
        a=b
        b=temp
    return b
x=fib(6)
print(x)
                         
