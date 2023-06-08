def fib(n,arr):
    if n==0 or n==1:
        return n
    if arr[n]!=0:
        return arr[n]
    arr[n]=fib(n-1,arr)+fib(n-2,arr)
    return arr[n]
arr=[0,0,0,0,0,0,0]
x=fib(6,arr)
print(x)
