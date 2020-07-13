a = int(input())

if (a % 4 == 0) and (a % 100 != 0 or a % 400 == 0):
    print(1)
else:
    print(0)

# 파이썬에서 논리연산자는 이렇게 사용한다. 헷갈 ㄴ.