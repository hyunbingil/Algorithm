n = int(input())
a = 0
b = 0
num = 1
m = 0

if not (0 <= n <=99):
    exit()

m = n # 새로운 변수에 처음 숫자를 넣어서 돌려야하는데
# 돌리는 곳 안에 새로운 변수 넣고 해서 무한으로 루프가 돌아갔었음 ㅠㅡㅠ
while True:
    b = n % 10
    a = int(n / 10)
    c = a + b
    n = (b * 10) + c % 10

    if (n == m):
        break
    else:
        num += 1    
print(num)
