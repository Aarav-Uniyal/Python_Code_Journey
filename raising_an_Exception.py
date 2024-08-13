name = input("Enter your name.\n")

if name.isnumeric():
    raise Exception("Numbers are not allowed.")

print(f"Hello {name}!")

# 1000 lines of code which takes much time.

a = int(input("Enter the first number.\n"))
b = int(input("Enter the second number.\n"))

if b == 0:
    raise ZeroDivisionError("Can't divide a number with zero.")

c = input("Enter your name(Once again!).\n")

try:
    print(d)

except Exception as e:
    if c == "Aditya":
        raise ValueError("Chinese are not allowed.")

    print("Exception Handled.")