# We can also open a file using with block.
# The advantage of using with block is that it automatically cloases the file.

with open("test.txt") as f: 
    a = f.readlines()
    print(a)

# f = open("test.txt", "rt")
# a = f.readlines()
# print(a)
# f.close()