class Employee:      # It is polite to start a class name
    no_of_leaves = 8 # with a capital letter.


Aarav = Employee()
Aditya = Employee()

Aarav.name = "Aarav"
Aarav.salary = 100000000
Aarav.job = 'Ethical Hacker'

Aditya.name = "Aditya"
Aditya.salary = 10
Aditya.job = 'Office Boy'

print(Aarav.__dict__) # .__dict__ will return a dictionary
                      # of a class's or object's instances.

Aarav.no_of_leaves = 9 # A class's instance will not change 
# if we try to change it through an object. Instead it will
# create a new instance for the object.
print(Employee.no_of_leaves) # The class's instance 
                             # is unchanged.
print(Aarav.__dict__) # But a new instance is created for the
                      # object.

print(Employee.__dict__)
Employee.no_of_leaves = 9 # We need to change a class's
                          # instance through a class only.
print(Employee.no_of_leaves)# The class's instance is changed.
print(Employee.__dict__)
print(Aditya.__dict__) # A class instance is not included in
                       # its object's dictionary.
                       