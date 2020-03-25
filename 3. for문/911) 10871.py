n, x = input().split()
n = int(n)
x = int(x)
A = list(map(int, input().split()))
# for 안에서 하나씩 받아서 x보다 작으면 A에 넣으려고 했는데
# 그렇게 되면 띄어쓰기로 숫자를 나눠서 인식해야하는데 엔터로 인식하게되더라..
# 그래서 그냥 밖에서 list로 받아버리고 print 하는 걸로...

for i in range(n):
    if A[i] < x:
        print(A[i], end=' ')