lst = ["Aarav","Aditya","Harshit","Anant","Harsh."]

# This is not efficient and also "and" comes at the end of the list, which is
# grammatically incorrect.

for i in lst: 
    print (i ,"and", end=" ")    

# Using join(), we can do this in an efficient way.
# Observe the syntax carefully.
print () # Ignore this, it is just for a new line after the for loop.

a = " and ".join(lst)
print (a)