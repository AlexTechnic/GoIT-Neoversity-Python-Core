# example of function with memoization (caching)
# this is a closure function that returns a function that makes calculation with caching

# function that returns a function that calculates the n-th fibonacci number 
def caching_fibonacci(): # this function will return inner function
    """
    Returns a function that calculates the Fibonacci sequence using caching.

    The returned function takes an integer `n` as input and returns the `n`th Fibonacci number.
    It uses a cache to store previously calculated Fibonacci numbers, which improves performance
    by avoiding redundant calculations.

    Returns:
        A function that calculates the Fibonacci sequence using caching.
    """

    cache = {} # dictionary to store the calculated fibonacci numbers

    def fibonacci(n: int) -> int: # inner function that calculates the fibonacci number
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    
    return fibonacci # return the inner function that makes calculation with previous cached values

# test of function with some values 
fib = caching_fibonacci() 
print(fib(10))  # 55
print(fib(15))  # 610
print(fib(20))  # 6765

# TODO: compare speed of the function with large values with timeit module wiht and without caching
