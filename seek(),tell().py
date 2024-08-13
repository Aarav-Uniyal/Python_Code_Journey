f = open("test.txt") # We don't need to specify the mode as "rt" is the default mode.
print(f.tell()) # This is used by the user to know where the character pointer is.
print(f.readline())
f.seek(11) # This is used to send the character pointer at a particual character place.
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()
  
