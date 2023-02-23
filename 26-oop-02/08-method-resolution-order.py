# Method Resolution Order (MRO) demo

# When a class is created, Python sets the MRO for that class
# Determines the ORDER that Python will look for methods on instances of that class

# 3 ways to programmatically reference the MRO:
# the __mro__ attribute of the class
# the mro() method of the class
# the built-in help(class) method -> the best way to view the MRO

class A:
    def do_something(self):
        print("Method defined in: A")


class B(A):
    def do_something(self):
        print("Method defined in: B")


class C(A):
    def do_something(self):
        print("Method defined in: C")


class D(B, C):
    def do_something(self):
        print("Method defined in: D")


print("Instantiate Class D into an object...")
thing = D()
print("Access inherited do_something() method...")
thing.do_something()

print("\nView MRO using __mro__ attribute of class D...")
print(D.__mro__)

print("\nView MRO using mro() method of class D...")
print(D.mro())

print("\nView MRO using help() method & passing the class D as argument value..")
print(help(D))

# Method Resolution Order (MRO) of demo code's do_something() method
# Class D -> Class B -> Class C -> Class A -> builtins.object

# Parentage structure of the do_something() method initially defined in Class A & inherited down to Class D
#       A
#      / \
#     B   C
#      \ /
#       D
