size=int(input("size:"))
l=[]
for i in range(size):
    ele=int(input("element:"))
    l.append(ele)
print(l)
for i in l:
    if(i%2==0):
        print(i)
    
