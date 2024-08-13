x = 5
y = 7

# Notice the def keyword before each function.

def func1(a,b): # Function without a return value.
    print ("Good Morning!",a+b)
def func2(a,b): # Function with a return value.
    '''This function will return the average.
It does not work for 3 or more numbers.''' # This is called a docstring. We can add it
                                                  # for the understability of a function.
                                                  # We can check this using ._doc_ method.
                                                  # See below:

    print ("Here is your average.")  
    return (a+b)/2  

print (func1(5,7)) # This will return None after the output as func1 does not have a return value.
func1(x,y) # We just need to call the function to avoid printing None :-)
func2(x,y)
print(func2.__doc__) # This will print the docstring of func2().

    