n = int(input())
case = []
a_list = []
b_list = []
k = 1
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    a_list.append(a)
    b_list.append(b)
    case.append(a+b)

for j in case:
    print('Case #%d: %d + %d = %d'%(k, a_list[k-1], b_list[k-1], j))
    k = k+1