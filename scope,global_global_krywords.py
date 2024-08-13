l = 10 # Global

def function1(n):
    l = 5 #Local
    m = 8 #Local
    global l # global keyword gives a function the permission to change the value
# of a global variable or permits a function to make a global variable(See below).    
    l = l + 45 # function1() cannot change global variable l if the global
               # keyword (global l) is not there.
    print(l, m)
    print(n, "I have printed")

function1("This is me")
# print(m)

x = 89
def aarav():
    x = 20
    def aditya():
        global x # This will change the value of global variable x from 89 to 88.
                 # If global variable x is not there, it will make one.
        x = 88
    print("before calling aditya()", x) # The global x will not affect the value
    # of local variable x in harry() as it is not a global variable.
    aditya()
    print("after calling aditya()", x) # The output is the same even after calling
                                       # function aditya().

aarav()
print(x) # This will output 88 as the value of global variable x is now changed
         # to 88 from 89 as function aditya() has been ran before printing x.