class A:
    var1 = "I am a normal variable in class A."

    def __init__(self):
        self.var1 = "I am an instance variable in class A."
        self.grade = "A"
        self.special = "I am a special variable."


class B(A):
    var1 = "I am a normal variable in class B."

    # The previous constructor in class A has been overrode, so,
    # there is no special variable now.
    # We can use super() so that the constructor of the super class (A)
    # runs first.
    def __init__(self):
        # This will call the constructor of the super class first.
        # Observe the syntax.
        super().__init__()
        # The instance variables' values of class A can now be changed as
        # done below.
        self.var1 = "I am an instance variable in class B."
        self.grade = "B"
        # If super() is called after changing the instance variables' values
        # the new constructor will become the exact copy of the old one.
        # The values of instance variables .var1 and .grade are changed now
        # but the .special is now included in class B's constructor.


a = A()
b = B()
# Python first searches for var1 as an instance variable in class B,
# then it searches for the same in class A. Then, it searches for a
# normal variable in class B and finally, in class A.
# If it cannot find the variable it throws an error.
print(b.var1)
print(b.grade)
# The previous constructor in class A has been overrode, so,
# there is no special variable now. So, this will throw an error.
# But if super() is used, it will not throw an error.
print(b.special)
