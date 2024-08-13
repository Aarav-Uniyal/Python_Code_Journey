f = open("test.txt","rt")# This will open test.txt in rt(read text) form and will assign it to f.
# print(f.readlines()) # This reads the file in a form of a list.
# print(f.readline()) # This is used to read a line of the file.
# print(f.readline())
# print(f.readline())
content = f.read() # This will read the file
print (content)

# for line in f: # Do not use for loop with .read() because it print spaces instead of data.
    # print(line, end="")

# content = f.read(34455) # 34455 is the no. of characters the read() function reads.
# print("1", content)

# content = f.read(34455)
# print("2", content)
f.close() # It is polite to close the file after opening it.
