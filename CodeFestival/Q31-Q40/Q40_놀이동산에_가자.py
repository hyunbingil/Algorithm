limit = int(input())
n = int(input())
member = []
count = 0
weight = 0
for i in range(0, n, 1):
    member.append(int(input()))

# member.sort()
for i in member:
    weight += i
    if (weight <= limit):
        count += 1

print(count)

# 다른 답
# total = 0
# count = 0
# limit = int(input())
# n = int(input())
 
# for i in range(n):
#     if total <= limit:
#         total += int(input())
#         count = i
# print(count)
