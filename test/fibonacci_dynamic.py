
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
    # n이 0이면 0 반환
    if n == 0:
        return 0
    # n이 1이면 1 반환
    elif n == 1:
        return 1
    # n의 값이 memo에 없으면 피보나치 수를 계산하고 memo에 저장
    elif n not in memo:
        memo[n] = fibonacci_dynamic(n - 1, memo) + fibonacci_dynamic(n - 2, memo) #키에다 값을 넣음
    # 피보나치 수 반환
    return memo[n] #리턴값은 정수

n = 20
# 처음 20개의 피보나치 수를 계산
fibonacci_sequence = [fibonacci_dynamic(i) for i in range(1, n + 1)]
# 피보나치 수열 출력
print(fibonacci_sequence)