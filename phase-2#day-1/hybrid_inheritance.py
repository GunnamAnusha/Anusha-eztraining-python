class parent:
    def pdisplay(self):
        print("I am a grand parent")
class child1(parent):
    def c1display(self):
        print("I am a child1 in 2nd genre")
class child2(parent):
    def c2display(self):
        print("I am a child2 in 2nd genre")
class kid1(child1):
    def k1display(self):
        print("I am a kid1 in 3rd genre")
class kid2(child1):
    def k2display(self):   
        print("I am a kid2 in 3rd genre")
class kidd1(child2):
    def kk1display(self):
        print("I am a kidd1 in 3rd genre")
class kidd2(child2):
    def kk2display(self):
        print("I am a kidd2 in 3rd genre")
d1=kid1()
d1.pdisplay()
d1.c1display()
d1.k1display()
d2=kid2()
d2.pdisplay()
d2.c1display()
       d2.k2display()
d3=kidd1()
d3.pdisplay()
d3.c2display()
d3.kk1display()
d4=kidd2()
d4.pdisplay()
d4.c2display()
d4.kk2display()
