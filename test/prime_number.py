def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 예시: 2부터 50까지의 소수를 구하기
prime_numbers = [x for x in range(2, 10) if is_prime(x)]
print(prime_numbers)



kkk = [kk**2 for kk in range(2, 10)]
print("==========")
print(kkk)


for i in range(5):
    print(i)




