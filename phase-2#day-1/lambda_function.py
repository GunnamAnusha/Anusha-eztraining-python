#lambda function
l=[1,2,3]
r=map(lambda x:x+1,l)
print(list(r))
#map-helps to create iteration,returns map object
res=map(lambda n:pow(n,2),l)
print(list(res))
name="anu"
(lambda name:print(name))(name)
