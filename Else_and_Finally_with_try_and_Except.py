f = open("Anant_Food.txt")

try:
    f1 = open("This_file_does_not_exist.txt")

# except Exception as e:
#     print(e)

except IOError as e: # We can add more than 1 except statements.
    print(e)

except EOFError as g:
    print(g)

else: # Else statement is only executed if the except one is not.
    print("The except statement was not executed.")

finally: # Finally will run anyway.
    # It is mainly used to close files and to clean up code.
    print("This will print anyway.")
    f.close()
