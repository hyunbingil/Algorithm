n = int(input())
star = '*'
real = n
blank = ' '
if n % 2 == 0:
    print()
for i in range(0,n):
    print(star * (i+1))