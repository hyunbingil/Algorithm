n = int(input())
m = list(map(int, input().split(' ')))

m.reverse()
for i in m:
    print(i, end=" ")