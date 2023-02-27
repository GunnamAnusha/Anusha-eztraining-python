#inherits from two base classes one child classes
#inherits properties from mom and dad

class mom:                #base class1
    def mdisplay(self):
        print("mom class")
class dad:              #base class2
    def ddisplay(self):
        print("dad class")
class child(mom,dad):
    def cdisplay(self):
        print("child class")
d=child()
d.cdisplay()
d.mdisplay()
d.ddisplay()
