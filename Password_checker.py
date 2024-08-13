print ("This is Atlan's Lair.","Enter your password below.")
a = input()
a = str(a)
i=0
while (i<=5):
    i=i+1
    if (a=="Atlan Aarav"):
        print ("Access granted.")
        break
    elif (i==5):
        print ("You have tried so many times. You cannot enter the password now.")
        break  

    else :
        print ("Access denied.","Try again.")
        a = input()
           