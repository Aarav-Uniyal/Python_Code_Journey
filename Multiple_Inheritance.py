
class Employee:
    no_of_leaves = 8
    var = 8

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

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game =game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

# Multiple inheritance is taking features from multiple classes.
# Note that the class written earlier in the arguments gains more importance.
# If the constructors, variables, attributes, etc. of the two classes collide,
# the first class is used.
# Hence, the order is important as it affects precedence.

class CoolProgramer(Player, Employee):
    var = 10
    language = "Python"
    def printlanguage(self):
        print(self.language)

Harsh = Employee("Harsh", 255, "Instructor")
Aditya = Employee("Aditya", 455, "Student")

Anant = Player("Anant", ["Cricket"])
Aarav = CoolProgramer("Aarav",["Chess"])

# Aarav.printlanguage()
# details = Aarav.printdetails()
# print(details)

# Python will first look for 'var' in the class itself then in the first class
# and the latter is checked in the last.
print(Aarav.var)

