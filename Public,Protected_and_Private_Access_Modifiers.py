
# Public - can be used by anyone.
# Protected - can be used by the subclasses of the class and cannot be accessed
# by outer classes.
# Private - by using _class_name__private_modifier.

class Employee:
    no_of_leaves = 8
    var = 8
    # This is protected.
    _protec = 9
    # This is private.
    __pr = 98

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

Aarav = Employee("Aarav", 100000000, "Programmer")
# We can print protected modifiers using normal method:
print(Aarav._protec)
# We can only access private modifiers using this method:
print(Aarav._Employee__pr)
