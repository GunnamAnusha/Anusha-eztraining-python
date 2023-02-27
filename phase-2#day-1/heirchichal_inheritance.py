class parent:
    def pdispaly(self):
        print("parent class")
class child1(parent):    #first derived class
    def c1display(self):
        print("I am one child")
class child2(parent):           #second derived class
    def c2display(self):
        print("I am second child")
d1=child1()
d2=child2()
d1.c1display()
d2.c2display()
 
