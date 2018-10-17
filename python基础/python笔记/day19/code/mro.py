# mro.py


class A:
    def go(self):
        print('A')
        # super().go()  # error

class B(A):
    def go(self):
        print('B')
        super().go()

class C(A):
    def go(self):
        print('C')
        super().go()

class D(B, C):
    def go(self):
        print('D')
        super().go()

d = D()
d.go()  # 





