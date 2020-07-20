def iter_factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(iter_factorial(5))