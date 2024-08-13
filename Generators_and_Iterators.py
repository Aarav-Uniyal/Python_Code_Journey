
"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration - processing of itering.

"""

# Generators help make iterators in an easy way.
# They generate values on-the-fly.
def gen(n): # This is a generator.
    for i in range(n):
        yield i # See the yield keyword.

g = gen(3)
# print(g.__next__()) # This will print the next value in the generator.
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

# h = 546546 # This will throw an error as int is not iterable.
h = "Aarav"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)


