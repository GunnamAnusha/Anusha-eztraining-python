#lets say u have lot of functions in your project
#u can give all definitions at one place
#easy to read,especially for others
#those who r seeing your program

print("before function")
def f1():
    print("f1")
    
def f2():
    print("f2")
    
def f3():
    print("f3")
if __name__=="__main__":
    f2()
    f1()
    f3()
print("name:",__name__)
