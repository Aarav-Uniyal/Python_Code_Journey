import random
random_number = random.randint(0, 1) # This will print a random number between 0 and 1.
print(random_number)
rand = random.random() * 100 # This will print a random number (including decimals) from 0 to
                             # 100 as we have written * 100 after the function. If we did not
                             # add * 100 the resulting random number would be between 0 and 1.
print(rand)
lst = ["Star Plus", "DD1", "Aaj Tak", "Colors"]
choice = random.choice(lst) # This will print a random content from the list given.
print(choice)
  
