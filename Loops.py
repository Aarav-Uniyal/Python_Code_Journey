# For loop:

# list1 = [ ["Harry", 1], ["Larry", 2],     # This is a nested list.
#           ["Carry", 6], ["Marry", 250]]
# dict1 = dict(list1)
#
# for item in dict1:
#     print(item)
# for item, lollypop in dict1.items():
#     print(item, "and lolly is ", lollypop)
items = [int, float, "Aarav", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)

# While loop:

i = 0
while (i <= 50):
    print (i) 
    i = i+1       

