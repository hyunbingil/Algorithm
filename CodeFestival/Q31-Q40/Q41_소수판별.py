def check_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i + 1
    if i == n:
        print("YES")
    else:
        print("NO")

check_prime(int(input()))                


# x = int(input())
# for i in range(2, x//2 + 1):
#     if x == 1:
#         print('소수가 아닙니다.')
#         break
#     if x == 2:
#         print('소수입니다.')
#         break
#     if x % i == 0:
#         print('소수가 아닙니다.')
#         break
# else:
#     print('소수입니다.')