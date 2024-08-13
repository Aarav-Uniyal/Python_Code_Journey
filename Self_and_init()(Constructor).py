class Employee:
    # This is a constructor. 'self' is the object which is passed.
    def __init__(self, name1, salary1, job1):
        # This will make the following instances for the object
        # passed in.
        self.name = name1
        self.salary = salary1
        self.job = job1
        pass
    
    # We can also use the object's instances in a function(See below).
    def Details(self):
        return f"The name is {self.name}, the salary is {self.salary} and the job is {self.job}."
# Syntax of using constructors:-
Aarav = Employee("Aarav", 100000000, 'Ethical Hacker')
print(Aarav.__dict__) # The instances have been constructed.
print(Aarav.Details())#This is how we call a method for an object.
# No need to add self, it takes the object automatically as self.