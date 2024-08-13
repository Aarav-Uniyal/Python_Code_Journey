import os
print(dir(os))
# This will print the current directory we are working on.
print(os.getcwd())
# This will change the current directory we are working on.
os.chdir("C:/")
print(os.getcwd())
# This will throw an error as Coroutines.txt is not in C:/
# f = open("Coroutines.txt")

# This will print all the files and folders in C:/ in the form of a list.
print(os.listdir("C:/"))
# This will make a directory/folder in the current working directory.
os.mkdir("Hello")
# This will make a 'this' directory/folder in the current working directory
# and will make a 'that' directory/folder in it.
os.makedirs("This/that")
# This method is used to rename a file.
os.rename("Coroutines.txt", "coroutines(test).txt")
# This will print all the components of environment variable 'Path'.
print(os.environ.get('Path'))
# This is use to join to paths(just joins them and prints to the console).
# Not really joins the path.
# It is mainly used because it automatically eliminates the extra slashes.
print(os.path.join("C:/", "/harry.txt"))
# This will tell whether the path exists or not.
print(os.path.exists("C:/Program Files2")) # This will return false.
print(os.path.exists("C:/Program Files")) # This will return true.
# This is used to check whether the file ius a directory or not.
# There are many other 'is' methods to check the type of the document.
print(os.path.isdir("C:/Program Files")) # This will return true.
