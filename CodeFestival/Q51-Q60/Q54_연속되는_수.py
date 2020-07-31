num = list(map(int,input().split(' ')))

num.sort()
result = 0
for i in range(0, len(num) - 1, 1):
    if num[i+1] == (num[i] + 1):
        result += 1

if result == (len(num) - 1):
    print("YES")
else:
    print("NO")

# user_input = input().split(' ')
# user_input = [int(i) for i in user_input]

# def sol(l):
#     l = sorted(l)
#     for i in range(len(l) - 1):
#         if l[i]+1 != l[i+1]:
#             return 'NO'
#     return 'YES'

# print(sol(user_input))