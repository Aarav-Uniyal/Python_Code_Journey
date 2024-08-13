class Employee:
    no_of_leaves = 8

    def __init__(self, name1, salary1, job1):
        self.name = name1
        self.salary = salary1
        self.job = job1
        pass

    # classmethod as alternative constructor.
    # We can also take a string as a parameter and then use it to make
    # a new object.
    @classmethod
    def alternative_constructor(cls, string):
        # .split() deletes the value passed in it and then makes a list of
        # the seperated new strings.
        # params = string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[3])
        return cls(*string.split("-"))  # We can also use this method.
        # Observe the symbol *.


Aarav = Employee.alternative_constructor("Aarav-100000000-Ethical Hacker")
print(Aarav.job)
