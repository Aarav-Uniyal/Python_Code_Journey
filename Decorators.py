def func1():
    print("Hi!")

func2 = func1 
del func1
func2() # func2 will work even if func1 is deleted as it has
        # become a copy of func1. 

# A decorator acts as a template and is used when we want
# to make a similar change to multiple functions.

def dec(func): # This is a decorator.
    def exec1():
        print("Executing now.")
        func()
        print("Executed.")
    return exec1 # When we use parentheses after a function
                 # it means that we are calling it.

@dec # This is another method of declaring a function to a
# decorator instead of func = decorator(func)(see below). 
def function():
    print("Hello!")

# function = dec(function)
function()