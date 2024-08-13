# List comprehension:

# lst = []                              # Multi-liner way
# for i in range(100):
#     if i%2==0:
#         lst.append(i)

lst = [i for i in range(100) if i % 2 == 0]  # Single-liner way
print(lst)

# Dictionary comprehension:

dic = {index: f"Person {index}" for index in range(1, 101)}
print(dic)

# Set comprehension:

set1 = {item for item in ["A", "B", "D", "A", "B"]*100}
print(set1)

# Generator comprehension:

gen = (i for i in range(100) if i % 3 == 0)
print(gen)
print(gen.__next__())
print(gen.__next__())

for item in gen:
    print(item)
