# Diamond shape problem:


class A:
    def met(self):
        print("This is a method from class A")


class B(A):
    def met(self):
        print("This is a method from class B")


class C(A):
    def met(self):
        print("This is a method from class C")


class D(B, C):
    def met(self):
        print("This is a method from class D")


a = A()
b = B()
c = C()
d = D()

# Python will first look for met() in D, then B (the class which
# comes first as an argument) then C and finally in A.
d.met()
