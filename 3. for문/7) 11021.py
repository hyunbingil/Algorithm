n = int(input())
case = []
k = 1
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    case.append(a+b)

for j in case:
    print('Case #%d: %d'%(k, j))
    k = k+1