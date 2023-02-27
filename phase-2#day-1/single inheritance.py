class A:
    n=30
    print(n//2)
class B(A):
    def calc(self):
        c=self.n+70
        print(c)
        print(c*2)
d=B()
d.calc()
