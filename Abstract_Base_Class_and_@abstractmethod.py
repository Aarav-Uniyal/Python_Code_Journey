# @abstractmethod is a method which we want to make a must for
# the subclasses of a class to have.
# But first we have to import some modules:

# from abc import ABCMeta, abstractmethod # Non-efficient method
from abc import ABC, abstractmethod  # Efficient method.


# This is a base class:

# class Shape(metaclass=ABC): # Non-efficient method
class Shape(ABC):  # Efficient method.
    @abstractmethod
    def printarea(self):
        # return 0 # We can also use this instead of pass.
        pass


class Rectangle(Shape):
    types = 2

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # Python will throw an error if we do not include this method.
    def printarea(self):
        return self.length * self.breadth


class Square(Shape):
    types = 1

    def __init__(self, side):
        self.side = side

    def printarea(self):
        return self.side * self.side


rec1 = Rectangle(2, 3)
sq1 = Square(5)
print(rec1.printarea())
print(sq1.printarea())
# We cannot make an object of a base class
# tryobject = Shape() # This will throw an error.
