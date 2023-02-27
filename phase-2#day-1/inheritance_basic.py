
#one parent and one child class
class parent:
    def display(self):
        print("i am superior")
#derived class
class child(parent):
    def show(self):
        print("i am junior")
c=child() #c is object for child class
c.display()
c.show()
