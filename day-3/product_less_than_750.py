l=list(map(int,input("numbers").split()))
print(l)
x=1
y=0
for i in l:
    x=x*i
    y=y+i
if(x<=750):
    print("product is:",x)
else:
    print("sum is:",y)
    
