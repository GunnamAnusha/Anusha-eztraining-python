import random as r
x="Pragti Engineering college"
print(r.sample(x,2))
a=[1,2,3,4,5]
r.shuffle(a)
print(a)
print(r.choice(a))
b="welcome back"
print(r.choice(b))
a=r.random()
print(a)
print(r.randint(20,30))
a=[10,20,30,40,50]
print(r.choices(a,k=10))
s="hello good day"
print(r.choices(s,k=3))
print(r.uniform(5,10))
z=dir(r)
print(z)
