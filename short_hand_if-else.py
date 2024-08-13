a = int(input("Enter A."))
b = int(input("Enter B."))

# We can also write our if-else statements in one line but this is not recommended as this 
# reduces the readability of the program.

# if a>b: print ("A is greater than B")
print ("A is greater than B") if a>b else print("B is greater than A.")