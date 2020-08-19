n = input()
n = int(n)
goMap = [[0 for col in range(20)] for row in range(20)] 

for i in range(n):
    x, y = input().split()
    goMap[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(goMap[i][j], end=' ')
    print('')