class Employee:
    no_of_leaves = 8
    def __init__(self, name1, salary1, job1):
        self.name = name1
        self.salary = salary1
        self.job = job1
        pass

    @classmethod # This is a class method whiich can be accessed by the
                 # class or its objects.
    # Observe the cls argument instead of self. It stands for class.             
    def Classmethod(cls, new_leaves ):
        cls.no_of_leaves = new_leaves
        pass
# We must not declare an object to a class if we are using constructors.

Aarav = Employee("Aarav",100000000,'Ethical Hacker')
Aarav.Classmethod(9)
print(Aarav.no_of_leaves)
print(Employee.no_of_leaves)
