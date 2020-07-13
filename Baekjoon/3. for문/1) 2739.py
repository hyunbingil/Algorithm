# 구구단

N = input()
N = int(N)
for i in range(9): # 숫자를 입력받아서 순서열을 만들어주는 내장 함수(Built in function).

    print(N, "*", i+1, "=", N*(i+1))
