# Operator overloading is using an operator to do multiple jobs for different texts.
# Dunder or magic methods are mainly used for operator overloading.
# For more dunder methods, go to this page:
# https://docs.python.org/3/library/operator.html

class Employee:
    def __init__(self, name1, salary1, job1):
        self.name = name1
        self.salary = salary1
        self.job = job1
        pass

    def details(self):
        return f"The name is {self.name}, the salary is {self.salary} and the job is {self.job}."

    # This is used to add two objects' instances
    def __add__(self, other):
        return self.salary + other.salary

    # This is used to divide two objects' instances
    def __truediv__(self, other):
        return self.salary / other.salary

    # This will give the detail of the object if the object is printed.
    # __repr__() is an alternative of __str__() (See below).
    # It will not work if __str__() is given. It will work only if it is called specifically.
    def __repr__(self):
        return f"Employee({self.name}, {self.salary}, {self.job})"

    # __str__() is same to __repr__() but it is given more importance.
    def __str__(self):
        return f"Name is {self.name}, salary is {self.salary} and job is {self.job}."



Aarav = Employee("Aarav", 100000000, 'Ethical Hacker')
Aditya = Employee("Aditya", 10, 'Office Boy')
print(Aarav + Aditya)
print(Aarav / Aditya)
# This will use __str__() method but if __str__() is not given, it will use __repr__().
print(Aarav)
# This will use __repr__() method.
print(repr(Aarav))
# This will use __str__() method but if __str__() is not given, it will use __repr__()
# even if we have called the str function.
print(str(Aarav))