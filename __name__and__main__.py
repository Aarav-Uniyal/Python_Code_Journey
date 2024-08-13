# When we import a file to another file, the content in the file also gets
# executed. To fix this, we can write the executable part of the file under
# if __name__ == "__main__": so that it only gets executed when the file having
# the content is ran. 

# If this file is imported to another file the comntent under 
# if __name__ == "__main__":  will not get executed.

import random
import time

def randomnum(n):
    rand = random.randint(0, n)
    print (f"The random number is {rand}.")

def time1():
    time2 = time.asctime(time.localtime(time.time()))
    print (f"The current time of your system is {str([str(time2)])}.")

i = int(input("Enter the number.\n"))
# The following line will print __main__ if the content is ran in the file
# itself. Otherwise, it will print the name of the file having the content. 
 
print("The file name is ",__name__)

if __name__ == "__main__":
    print ("I am calling my functions now.")
    randomnum(i)
    time1()
    pass


