
# initial function
# def fibonacci(n):
    # starting cases
#    if n == 1:
#        return 1
#    elif n == 2:
#        return 1
#    elif n > 2:
#        return (fibonacci(n - 1) + fibonacci(n - 2))


# memo using a dic
# fib_cache = {}

# def fib_2(n):
    # if we have cached the value, we return it
#     if n in fib_cache:
#         return fib_cache[n]
    
    # compute nth term
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fib_2(n - 1) + fib_2(n - 2)
        
    # cache value to dict
#     fib_cache[n] = value
#     return value
  
  
# memoization using an in-built cache

# import Least Recently Used Cache
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fib_3(n):
    #checker of input
    if type(n) != int:
        raise TypeError("'n' must be a positive int")
    if n < 1:
        raise ValueError("'n' must be a positive int")

    #compute nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib_3(n - 1) + fib_3(n - 2)
    
    
for n in range(1, 1001):
#    print(n, ":", fibonacci(n))
#    print(n, ":", fib_2(n))
    print(n, ":", fib_3(n))
