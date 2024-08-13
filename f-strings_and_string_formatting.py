import math

me = "Aarav"
a1 =3

# Ways of formatting a string:

# a = "this is %s %s"%(me, a1) # Not efficient.

# a = "This is {1} {0}" # This will swap me to 0 and a1 to 1 as Python starts counting from 0.
# b = a.format(me, a1)  # Not efficient.
# print(b)

# F strings
a = f"this is {me} {a1} {math.cos(65)}" # Efficient.
print(a)                                # We can also add a function or operation in a f-string.
