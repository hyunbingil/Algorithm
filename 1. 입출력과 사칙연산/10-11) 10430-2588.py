# 10430 나머지
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

print(int((a+b)%c))
print(int((a%c + b%c)%c))
print(int((a*b)%c))
print(int((a%c * b%c)%c))

# 2588 곱셈
a = int(input())
b = int(input())
print(a*(b%10))
print(a*((b//10)%10))
print(a*((b//100)))
print(a*b)
# 수학...잘해야한다는 말을 체감합니다..^...^