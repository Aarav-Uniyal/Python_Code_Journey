class Employee:
    no_of_leaves = 8
    def __init__(self, name1 , salary1 , job1):
        self.name = name1
        self.salary = salary1
        self.job = job1
        pass

    # We can create a staticmethod if we want to do not want to take self
    # or cls as an argument. They are only accessible by the class and 
    # its objects.
    
    @staticmethod
    def Codename(codename):
        print("The codename of Aarav is " + codename + ".")

Aarav = Employee("Aarav", 100000000 , 'Ethicl Hacker')
Aarav.Codename("Atlan")        