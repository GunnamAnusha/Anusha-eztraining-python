#protected
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("encap function-accessing protection")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)

#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("encap function")
        print(self.__a)
obj=encap()
obj.encapfunction
()
print(obj.__a)#will throw error becoz a is private, can't be acessed outside class

#public
class encap:
    a=10
    print(a)
    def encapfunction(self):
        print("encap function")
    
