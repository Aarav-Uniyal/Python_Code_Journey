from time import sleep
from functools import lru_cache

# @lru_cache saves the result of a function as cache.
# So, the next time we call the similar function with same input
# and output value, it does not run the function, just returns the value.
@lru_cache(maxsize=3) # maxsize is the no. of last calls you want to save.
                      # in your memory.
def Time(n):
    sleep(n)
    return n

print("Calling function...")
Time(3)
print("Done.")
print("Calling function...")
# This will take 4 seconds as the last function had 3 as input.
Time(4)
print("Done.")
print("Calling function...")
# This will take 2 seconds as the last function had 4 as input.
Time(2)
print("Done.")
print("Calling function...")
# This will not take 3 seconds as we have called the function earlier.
Time(3)
print("Done.")