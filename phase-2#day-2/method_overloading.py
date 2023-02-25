#method overloading
class m_overload:
    def display(self,a=None,b=None):
        print(a,b)
obj=m_overload()
print("without arguments")
obj.display()#without arguments
print("with arguments")
obj.display(20,30)#with arguments
print("with one argument")
obj.display(10)#with one argument
