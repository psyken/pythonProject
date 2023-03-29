def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10
fibonacci_sequence = [fibonacci_recursive(i) for i in range(1, n + 1)]
print(fibonacci_sequence)



def fibonacci_dynamic(n, memo={}):
    print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n not in memo:
        memo[n] = fibonacci_dynamic(n - 1, memo) + fibonacci_dynamic(n - 2, memo)
    return memo[n]

n = 20
fibonacci_sequence = [fibonacci_dynamic(i) for i in range(1, n + 1)]
print(fibonacci_sequence)