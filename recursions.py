# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
def factorial_iterative(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1) # The actual parameter n-1 will act as 
                                            # an argument in factorial_recursive().
    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120

# 0 1 1 2 3 5 8 13 # Fibonacci series.
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


number = int(input("Enter then number"))
# print("Factorial Using Iterative Method", factorial_iterative(number))
# print("Factorial Using Recursive Method", factorial_recursive(number))
print(fibonacci(number))
  
