class america:
    def placename(self):
        print("america!wow")
    def student(self):
        print("anu")
    def which_year(self):
        print("1st year M.S")
class canada:
    def placename(self):
        print("canada!good enough")
    def student(self):
        print("anusha")
    def which_year(self):
        print("2nd_year")
obj_ame=america()
obj_can=canada()
for details in(obj_ame,obj_can):  #we had called both the methods at a time,
    #so that the time complexity and space complexity had decreased and efficiency increased
    details.placename()
    details.student()
    details.which_year()
