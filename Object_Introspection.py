# Object introspection means to inspect an object.

class Employee:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        return f"The employee's name is {self.name}."


Aarav = Employee("Aarav")
# This will print the class of the object.
print(type(Aarav))
# This will print the id of the object.
print(id(Aarav))
# This will print all the instances and methods of the object.
print(dir(Aarav))

import inspect

# This will print all the details of the object.
# .getmembers() is a method in inspect module.
print(inspect.getmembers(Aarav))
