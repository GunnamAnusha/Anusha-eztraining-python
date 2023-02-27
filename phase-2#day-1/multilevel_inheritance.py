
class grandparent:
    def display(self):
        print("grand pa class")
class parent(grandparent):
    def show(self):
        print("parent class")
class child(parent):
    def printing(self):
        print("child class")
d=child()  #c is the object for child class...
d.display()
d.show()
d.printing()
                
