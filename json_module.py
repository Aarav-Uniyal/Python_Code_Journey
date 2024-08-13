# The json(JavaScript Object Notation) module is mainly used to convert the
# python dictionary into a JSON string that can be written into a file.

import json

data1 = '{"var1":"Variable1","var2":"Variable2"}' # Observe the single quotes.
# This will throw an error as we can only access a string using integers.
# print(data1['var1'])
print(data1) # This is a python string.

parsed = json.loads(data1) # This will change the python's string(dictionary) to a
                           # Javascript's dictionary.

print(type(parsed)) # 'parsed' is now a dictionary.
print(parsed['var1']) # We can now access the elements of the dictionary.
print(parsed) # 'parsed' has now been converted to a Javascript's dictionary.

data2 = {"name":"Aarav",
        "class":8,
        "parents":("Laxmi","Bhuwanesh"),
        "fav_games":["Minecraft","COD:Mobile"],
        "boy":True}

jscomp = json.dumps(data2) # This will format the python's dictionary to
                           # Javascript's string(dictionary).

print(jscomp) # 'jscomp' has now been converted to a Javascript's dictionary.

# The json.load() is used to read the JSON document from file.

# Use the sort_keys parameter to specify if the result should be sorted or not:
# json.dumps(x, indent=4, sort_keys=True)
# This will sort the result in alphabetical order.
