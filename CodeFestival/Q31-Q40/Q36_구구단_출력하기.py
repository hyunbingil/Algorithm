n = int(input())
arr = []
for i in range(0, 9, 1):
    m = n * (i+1)
    arr.append(str(m))

arr = ' '.join(arr)
print(arr)

# n = int(input())
# for i in range(1, 10):
# 	print(n*i, end = ' ')