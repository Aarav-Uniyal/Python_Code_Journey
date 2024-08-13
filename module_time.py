import time
initial = time.time()

k = 0
while(k < 45):
    print("I am Atlan Aarav.")
    time.sleep(2)  # This will print the next statement after an
    # interval of 2 ticks(seconds).
    k += 1
print("While loop ran in", time.time() - initial, "Seconds")
# This will subtract the initial(old) time from the current time.

initial2 = time.time()
for i in range(45):
    print("I am Atlan Aarav.")
print("For loop ran in", time.time() - initial2, "Seconds")


localtime = time.asctime(time.localtime(time.time()))
# This will output the time in the following format:
# Day Month Date Time(Hours:Minutes:Seconds) Year
print(localtime)
