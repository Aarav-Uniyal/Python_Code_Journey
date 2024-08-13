dict1 = {"Aarav":"Hacker",
         "Aditya":"Gamer",
         "Harshit":"Dancer",
         "Anant":"Cricketer"}

for keys in dict1:
    print(keys)
    # If break statement is executed in a loop, the else statement is not ran.
    # break

else: # An else statement is printed once the loop ends.
    print("The loop ran successfully.\n")

i = 0
while i < 1 :
    print(dict1.keys())
    i += 1

else:
    print("The loop ran successfully.\n")