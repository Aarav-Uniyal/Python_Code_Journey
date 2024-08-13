class Student: # Syntax of a class. There's no need to add
    pass       # pass but as we are making an empty class,
               # we have to add it.

Aarav = Student() # Declaration of an object.
Aditya = Student()

# We can add data of any type to an object.
Aarav.name = "Aarav" # Syntax of creating an attribute of
Aarav.std = 8        # an object.
Aarav.fav_subjects = ["Science", "Computer"]

Aditya.name = "Aditya" # It is not necessary to make the same 
Aditya.section = 'D'   # instances for objects belonging
Aditya.num_friends = 4 # to the same class.

print(Aarav.fav_subjects , Aditya.num_friends)
