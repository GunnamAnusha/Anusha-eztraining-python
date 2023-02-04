#usage of constructor
#constructor will make the objects alive like using (__init__)
class Employee:
    def __init__(self,name,number):
        self.number=number
        self.name=name
    def display(self):
        #print("number:%d \nName:%s" %(self.number,self.name))
        print(self.number,self.name)#logic-2 for printing in same line 
emp1=Employee("Anu",100)#same order should be maintained as in class arguments 
emp2=Employee("Annie",98)
emp1.display()
emp2.display()
