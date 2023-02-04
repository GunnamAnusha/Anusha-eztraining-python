#variables and var_acesss in class and method
class computer():
    a=10
    b=20
    print("class variable inside a class",a)
    def config(self):#config is a function  #self will point to the object for the class
        c=100
        print("yes")
        print("Instance acess",self.b)
lenova=computer()#object 1
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()#object 2
print("dell",dell.b)
dell.config()
