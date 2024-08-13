# Lambda functions or anonymous functions are one-line functions.
# They are just used for convenience so they are not an essential in Python.
# def add(a, b): # This is not a regular function.
#     return a+b

# minus = lambda x, y: x-y # This is a lamda function. minus is the function name. 
# Observe the syntax carefully.

# def minus(x,y): # This is a regular funcion which can be used instead of lambda.
#     return x-y

# print(minus(9, 4))
# def a(x): # This is a regular funcion which can be used instead of lambda.
    # return x[1]

a =[[1, 14], [5, 6], [8,23]] # This is a nested lst.
a.sort(key=lambda x:x[1]) # key takes a function for a list.
                          # It is used in .sort(). 
print(a) # The list has now been sorted to [[5,6],[1,14],[8,23]].