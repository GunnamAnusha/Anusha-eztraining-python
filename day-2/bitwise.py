a,b=int(input("enter a:")),int(input("enter b:"))
if(a|b<=15):
    c=a&b
    d=a|b
    e=a^b
    print("and:",c)
    print("or:",d)
    print("xor:",e)
else:
    print("number exceeded")
    
