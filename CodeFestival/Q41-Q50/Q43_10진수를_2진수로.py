# 내가 푼 방법 : 재귀
n = int(input())
array = []
def to_binary(m, arr):
    arr.append(str(m % 2))
    m = m // 2
    if m == 0:
        arr.reverse()
        arr = ''.join(arr)
        return print(arr)
    else:
        to_binary(m, arr)

to_binary(n, array)

# 답안 : 반복문
# a = int(input())
# b = []

# while a:
#     print(a)
#     b.append(str(a % 2))
#     a = int(a / 2)

# print(b)
# b.reverse()
# print(b)
# print(''.join(b))
