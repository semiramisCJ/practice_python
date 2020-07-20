def iter_fibonacci(n):
    before = 0
    current = 1
    i = 1
    while i < n:
        result = before + current
        i+=1
        before = current
        current = result
    return result

print(iter_fibonacci(6))