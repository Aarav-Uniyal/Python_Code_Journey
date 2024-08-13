l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

# Basic method of removing items at even index from a list:
# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Jarvis please buy {item}")
#     i += 1
# Method of removing items at even index with enumerate from a list:
for index, item in enumerate(l1):
    if index%2==0:
        print(f"Jarvis please buy {item}")


  
