import time
def dynamic_fibonacci(n, memo={}):
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except KeyError:
        result = dynamic_fibonacci(n-1, memo) + dynamic_fibonacci(n-2, memo)
        memo[n] = result
    return result

if __name__ == "__main__":
    initial_time = time.time()
    print(dynamic_fibonacci(int(input('Indica el numero a calcular: '))))
    final_time = time.time()
    print(final_time - initial_time)
