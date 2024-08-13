
class Employee:
    no_of_leaves = 8

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


# Single inheritance means to take the features of other class.
# Observe the parentheses and the class's name inside it.

class Programmer(Employee):
    no_of_holiday = 56
    # def __init__ is showing warning because we can use super().
    # For more information, refer to 'Super()_and_Overriding.py'.

    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



Harsh = Employee("Harry", 255, "Instructor")
Aditya = Employee("Rohan", 455, "Student")

Anant = Programmer("Shubham", 555, "Programmer", ["python"])
Aarav = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
print(Aarav.no_of_holiday)

