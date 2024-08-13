# Difference between *args and **kwargs:

# *args passes variable number of non-keyworded arguments list and on which 
# operation of the list can be performed. **kwargs passes variable number 
# of keyword arguments dictionary to function on which operation of a 
# dictionary can be performed.

# def function_name_print(a, b, c, d, e): # This is a normal function with
# limited arguments.
#     print(a, b, c, d, e)

# As a normal function can pass limited arguments, we can use *args and
# **kwargs to pass a list so that it does not have limited arguments.

# *args begin with * symbol and **kwargs begin with ** symbol (See below).


def funargs(normal, *argsrohan, **kwargsbala):  # The rule of passing
    # arguments is first normal arguments then *args and finally **kwargs.
    print(type(argsrohan))  # The passed list becomes a tuple.
    print(normal)
    for item in argsrohan:  # We don't need to write * symbol now.
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():  # We don't need to write ** symbol now.
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf",  # We don't need to write * symbol.
       "Hammad", "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan": "Monitor",  # We don't need to write ** symbol.
      "Harry": "Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}
funargs(normal, *har, **kw)  # Do not forget to add symbols before arguments.
