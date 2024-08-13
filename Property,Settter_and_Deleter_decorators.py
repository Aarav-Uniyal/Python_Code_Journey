class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"
        pass

    def details(self):
        return f"The name is {self.fname} {self.lname}."

    # We have to use parentheses after email in order to call it which offenses the
    # rule of encapsulation. Therefore, in order to use a method as an attribute, we
    # use a @property decorator.
    @property
    def email(self):
        # This will be returned if the attribute is deleted.
        # if self.fname == None or self.lname == None: # Another method of doing this task.
        if self.fname is None or self.lname is None:
            return f"Email not set."
        return f"The email ID is {self.fname}.{self.lname}@gmail.com"

    # This will set the values of fname, lname and email to the new fname, lname and email.
    # In this the email is the method to be made.

    @email.setter
    def email(self, newemail):

        names = newemail.split("@")[0]
        splitname = names.split(".")
        self.fname = splitname[0]
        self.lname = splitname[1]

    # Python cannot delete Aarav.email without a deleter.
    # In this the email is the method to be made.

    @email.deleter
    def email(self):
        # This will set the value of email as None.None@gmail.com.
        # To avoid this, we need to declare a conditional statement in email().
        self.fname = None
        self.lname = None


Aarav = Employee("Aarav","Uniyal")

# print(Aarav.email()) # We have to use parentheses to call the email method.
print(Aarav.email) # Using @property decorator, we do not need to use parentheses.

# This will throw an error if we have not declared a setter.
Aarav.email = "Atlan.Aarav@gmail.com"

# This will throw an error if we have not declared a deleter.
del Aarav.email
print(Aarav.email) # This will now print 'Email not set.'.
