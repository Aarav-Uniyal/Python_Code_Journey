# Warning : The pickle module is not secure.
# Only unpickle data you trust.

# pickle module is used to preserve a Python object in the memory.
# It can either be done by pickling an object to a file(using
# .dump and .load) or;
# saving the object in bytes(using .dumps and .loads).
# The data obtained by pickling is in binary format.

import pickle

# Pickling with a file.

# list1 = ["Aarav","Bhuwanesh","Laxmi"]

# with open("pickle(test).pkl","wb") as file: # or "ab"
#     pickle.dump(list1, file)

with open("pickle(test).pkl","rb") as file2:
    family = pickle.load(file2)
    print(family)
    print(type(family))

# Pickling without a file.

list2 = ["Aditya","Anant","Harshit","Harsh"]

bytes_data = pickle.dumps(list2)  # type(b) gives <class 'bytes'>

friends = pickle.loads(bytes_data)
print(friends)
print(type(friends))
