a = 10
b = 20
# 둘을 변경 해야 함 3번째 변수를 쓰지 않고

c = a
a = b
b = c

print(a+" : "+b)


a = 10
b = 20

a, b = b, a  # a와 b의 값을 서로 바꾸기

print(a, b)  # 출력: 20 10