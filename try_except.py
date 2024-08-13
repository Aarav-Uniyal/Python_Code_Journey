a = input("Enter the first number.\n")
b = input("Enter the second number.\n")

# We can use try and except to execute the entire program even if there is an error.
try:
    print ("The sum is",
           int(a)+int(b))
   
except Exception as e: # This line stores the Exception(error) in e and the prints e(now error).
    print(e)           # So, the program will not stop now.

print ("This line is very important.") # This line will be executed even if there is an error.   