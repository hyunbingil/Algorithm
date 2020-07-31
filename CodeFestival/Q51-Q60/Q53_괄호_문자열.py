bracket = list(input())
left = 0
right = 0
for i in range(0, len(bracket), 1):
    if bracket[i] == '(':
        left += 1
    elif bracket[i] == ')':
        right += 1

if left == right:
    print("YES")
else:
    print("NO")    

# def math(e):
#     if e.count('(') != e.count(')'):
#         return False
#     괄호 = []
#     for i in e:
#         if i == '(':
#             괄호.append('(')
#         if i == ')':
#             if len(괄호) == 0:
#                 return False
#             괄호.pop()
#     return True

# n = input()
# if math(n) == True:
# 	print("YES")
# else:
# 	print("NO")