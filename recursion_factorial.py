def factorial(n):
    """Return the factorial of n by a recursive approach"""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))