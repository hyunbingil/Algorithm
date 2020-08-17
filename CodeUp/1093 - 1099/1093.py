n = int(input())
m = list(map(int, input().split(' ')))

arr = []
count = 0

result = ''
for i in range(1, 24):
    arr.append(i)

for i in arr:
    for j in m:
        if i == j:
            count += 1

    if i == len(arr):
        result += str(count)
    else:    
        result += str(count)+' '

    count = 0

print(result)
