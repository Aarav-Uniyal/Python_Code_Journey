# string.endswith() : This function allow the user to check whether the given string ends 
# with passed argument or not. It returns True or False.
# string.count() : This function counts the total no. of occurrence of any character
# in the string. It takes the character whose occurrence you want to find as argument.
# string.capitalize() : This function capitalize the first character of any string. 
# It doesn’t take any argument.
# string.upper() : It returns the copy of string converted to upper case.
# string.lower() : It returns the copy of string converted to lower case.
# string.find() : This function finds any given character or word in complete 
# string. It returns the index no. of that character or word.
# string.replace(“old_word”, “new_word”) : This function replaces the
# old word or character with new word or character in complete string.
#string.isalnum() : This will return true if the string is an alphanumeric string or will return 
# false if the string is not.
mystr = "Aarav is a hacker."
# print(len(mystr))
# print (mystr[0:5:2]) # This will print the characters from 0 to 4 while skiping one character.
                       # The output would be Arv.  
# print(mystr[::-2]) # This will print all the characters from the back skipping 1 character.
                   # Output will be .echas aa

print(mystr.endswith("bdoy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.replace("is", "are"))
