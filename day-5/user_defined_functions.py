#without arguments and withoutreturn
"""def sample():
    print("Anusha")
    print("learning")
sample()
print("Pragati")
sample()"""

#without arguments and with return
"""def  multi():
  n1=int(input("number1: "))
  n2=int(input("number2: "))
  prod=n1*n2
  return prod
res=multi()
print(res)"""


#with argument and with return ##static input
"""def multi(n1,n2,n3)
    prod=n1*n2*n3
    return prod
res=multi(3,4,5)
print(res)"""


#with arguments and with return
"""def multi(a,b,c):
    prod=a*b*c
    return prod
n1=int(input("enter 1:"))
n2=int(input("enter 2:"))
n3=int(input("enter 3:"))
res=multi(a,b,c)
print(res)"""

#with arguments and without return
"""def multi(a,b,c):
    prod=a*b*c
    print(prod)
n1=int(input("enter 1:"))
n2=int(input("enter 2:"))
n3=int(input("enter 3:"))
res=multi(n1,n2,n3)
print(res)"""

#lemon program without arguments and without return
"""def  check():
    req=21
    lem=int(input("enter lemons:"))
    if(req==lem):
        print("you are sufficient")
    elif(lem<=req):
        print("not suffcient")
        s=req-lem
        print("need :",s)
    else:
        print("more than enough")
        print("exceeded by:",s)
check()"""



#factors of given number without argumets and without return
"""def factors(n):
   for i in range(1,n+1):
      if n%i==0:
      count+=1
        print(i)
n=int(input("number:"))
factors(n)"""


#table using with arguments and without return
"""def table(n):
    
  for i in range(1,11):
     print(i,"x",n,"=",i*n)
a=int(input("enter your number:"))
 
res=table(a)
print(res)"""

#sum of digits using with argument with return
#logic-1
"""def addition(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    return sum
n=int(input("enter number"))
print(addition(n))"""

#logic-2
def digits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
n=int(input("enter the number:"))
res=digits(n)
print(res)
    

    

   


  













    






