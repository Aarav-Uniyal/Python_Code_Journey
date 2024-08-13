import math # Import is like include and math is a module which is like a header file.

# print ("Hello world!\n")
# print (7+9)
# print (math.gcd(8,72)) # This will print the gcd(greatest common divisor) of 8 and 72.
# This is a single line comment.
'''
This is a 
   multi-line comment.

'''
# a = 43      # Variables are created in Python without mentioning the data type of the variable.
# b = "Aarav"
# c = 56.78
# print (a + c)
# print (type(a)) # type(variable_name) is used print the data type of a variable.
# a = "Str" # We can also change the value or data type of a variable
         #later(Do not use it before type()).
# print (type(a))
# print (a)
# e = "35"   # These will work as these are convertible to another data type.
# e = str(455)
# e = float("34")
# e = int(e)
# e = "53python" This will throw error as 53python is not convertible to an int.
# e = int(e)
# print (e+4)
# name = '''Aarav is a
# dangerous hacker''' # ''' can also be used like double quotes to print multi-line strings.
# print(name)
# name2 = "AaravU"
# print (name2[0]) # This will print the first character of name. This is like printing the first
                 # element of an array
# print (name2[2:5])  # This will print the characters from 2 to 4 index(rav in name2).
# string = '   Atlan   ' # We can also use '' instead of "" when assigning strings to variables.
# print (string.strip()) # .strip() is used to remove all spaces from the string.
# print (len(name2)) # len() is used to get the length of a string.
# print (string.lower()) # .lower() is used to set the case of a string in lower case.
# print (string.upper()) # .upper() is used to set the case of a string in upper case.
# print (string.replace("an", "m")) # .replace() is used to replace a or some characters with
                                  # another new character or characters.
# print (string + name2) # We can fuse two strings together by using a +.
# temp = "He is {} and {}.".format(string, name) # We can create a template by using
                   # these methods. The {} are a bit like data specifiers.
# temp = f"He is {string} and {name}." # Notice the f before the string.
# temp = "He is {0} and {1}.".format(string, name) # By default, the upper case is like this.
# temp = "He is {1} and {0}.".format(string, name) # We can exchange the values by this method.
# print (temp)
# The following are extra operators:
# 1. ** <--- exponent operator <--- This will multiply a number with its exponent (2**3 will give 8)
# 2. // <--- floor division    <--- This will always return an integer as quotient.
# 3. %  <--- modulo operator   <--- This will return the remainder of division.
# There are 4 types of collections in Python:-
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary
# lst = [64,56,78,99,100]  # Lists are like arrays.
# print (type(lst))
# print (lst)
# print (lst[0]) # We can access a particular element of a list just like an array.
# lst[2] = 65 # We can change the value of an element later.
# print (lst[1:4]) # Note that Python ignores the last no. (4 in this case) So, only the elements
                 # from 1 to 3 will be printed.
# print (len(lst)) # This will print the length of the list(here, lst).
# lst.append(100)  # .append() will add a element at the back of a list just like .push_back().
# lst.insert(1,99) # .insert() is used to add an element at a specific index in a list.
                 # 1 is the index and 99 is the element to be added to the list.
# lst.remove(56) # .remove() is used to remove a specific value from a list.
# lst.pop() # .pop() is used to remove a value from the back of a lit. No parameters are needed for .pop().
# del lst[3] # del list_name[index] is used tpo remove an element froma specific index. del = delete
           # We can also delete another things using del keyword.
# lst.clear() # .clear() is used to clear all the elements from a list.
# print(lst)
# Syntax bof a tuple. Note the parentheses.
# tupl = ("Aarav" , "Aditya" , "Harshit") # We cannot change the values withn a tuple.
# print (type(tupl))
# print (tupl)
# tupl = list(tupl) # We can do typecasting  to convert a tuple into a list or vice-versa.
# print (type(tupl))
# print (tupl)
# Syntax of a set:-
# sett = {3,3,4,5,4,4,5,5,5,3,5,3,3} # Notice the repeated values in the index.
# A set is used to remove the repeated values from an index. Note the curly braces.
# print(sett) # The output will be {3,4,5}
# sett.add(4499) # .add() is used to add a value at the back of a set.
# sett.update([4354,656,657,464]) # .update() is used to add multiple elements at the back of a set.
                                  # Notice the blocky braces.
# sett.remove(656) # We can also use .remove() function in a set.
# sett.discard(7777) # .discard() is like .remove() but it does not throw an error when an element
                   # which is not present in the set is said to be removed.
                   # .remove(888) <--- This will throw an error as 888 is not present in the set.
# print (sett)
# A dictionary is somewhat like a structure.
# Syntax of a dictionay :-
# dic = {

      #  "Aarav" : "Hacker",
      #  "Class" : 8,
      #  "Grade" : "D",
      #  "Marks" : 99.99,

      #  }
# dic["Marks"] = 100.0 # We can also change the value of a dictionary's element.
# print(dic["Grade"])  # We can access an element of a dictionary like this.
# dic.pop("Grade") # This will remove the Grade element including 8 from this dictionary.
# print (dic)
# age = input("Enter your age.\n") # input() is like scanf(). Observe the initialization.
# age = int(age) # We need to convert the string into an integer.
# if (age>18):
   # print("You can drive a car.") # There are no curly braces in if-else statements in
                  # Python. Everything which comes under the indentation is executed.
                  # (Observe the gap between column 0 and print, this is indentation.)
# elif (age==18):
   # print ("You have to make a driving license to drive a car.") # elif is like else if.
# else :
   # print ("You cannnot drive a car.")
# For loop syntax:-
# for i in range(0, 100): # This will print numbers from 0 to 99.
   # print (i)
# We can also iterate a list, tuple, set and dictionary like this:-
# lis = [34, 56 , "Aarav"]
# for item in lis: # This will output every item in lis.
   # print (item)
# While loop syntax:-
# i=0
# while(i<10):   # While loop syntax in python is very similar to the one in C.
   # This will print the numbers from 1 to 10.
   # i = i+1
   # if i == 5: # This will skip the number 5.
      # continue
   # if i == 7:
   #    break # This will break the loop.
   # print(i)
# Functions in Python are like C.
# Function syntax in Python:-
# def greet(): # Functions with no parameters and no return value.
   # print ("Good Morning Boss.")
   # greet()
# def product(a = 5, b): # Function with parameters and a return value. Here a is a default argument.
   # print ("Printing your product:")
   # c = a + b
   # return c
# print (product (3 , 6)) # This will print the product of 3 and 6.
# Syntax of class:-
# class employee:
   # def __init__(self, gname, gsalary): # Syntax of a constructor. self is necessary.
      # self.name = gname
      # self.salary = gsalary

# Aarav = employee("Aarav", 50000000)
# print (Aarav.name)
# print (Aarav.salary)

# print ("Aarav is a hacker. ") # The 2nd line will come in another line in the console.
# print ("He will hack your account.")

# print ("Aarav is a hacker. ", end="") # ,end="" is used to merge the two lines.
# print ("He will hack your account.")
# We can add anything betwwen the double quotes in ,end="," example we can add a comma (,) between the
#  two lines.
# We can also write this to merge two lines:-
# print ("Aarav is a pro gamer","and he will K.O. you." )
# We don't need to add a space after a line as Python will automatically add a space.
# print(10 * "Hello Boss.\n") # This will print Hello Boss ten times.
# a = 16
# b = 56
# print (10 * str(int(a)+int(b)))








