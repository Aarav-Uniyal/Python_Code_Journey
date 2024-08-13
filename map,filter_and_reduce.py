# --------------------------MAP------------------------------

numbers = ["3", "34", "64"]
# map() is used to apply a function on all elements of a thing.
numbers = list(map(int, numbers))  # We must write list() before map
# if we want to return the value as a list. 

# We have used len() after range() as range() only takes int as value.
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])

# def sq(a):
#   return a*a

num = [2, 3, 5, 6, 76, 3, 3, 2]


# square = list(map(sq, num))
# print(square)
# square = list(map(lambda x: x*x, num)) # Using map() with lambda.
# print(square)


def square(a):
    return a * a


def cube(a):
    return a * a * a


# We don't need to write the parentheses (See below to know why).
func = [square, cube]
for i in range(5):
    # This will run the functions square() and cube() for no.s in range(5).
    val = list(map(lambda x: x(i), func))
    print(val)

# --------------------------FILTER------------------------------
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_greater_5(num):
    return num > 5  # This will return True if the no. is greater than 5
    # otherwise it will return False.


# filter(), as the name says, is used to filter the data.
# Note the absence of parentheses.
# filter() returns an iterator yielding those items of iterable for 
# which function(item) is true.
# This will only print the numbers which are greater than 5.

gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)
# # --------------------------REDUCE------------------------------
from functools import reduce  # We have to import the reduce function.

list1 = [1, 2, 3, 4, 2]
# reduce() is used to apply a function of two arguments cumulatively
# to the items of a sequence, from left to right, so as to reduce 
# the sequence to a single value.

num = reduce(lambda x, y: x + y, list1)
n = 0
for i in list1:
    n = n + i
    print(n)
print(num)
