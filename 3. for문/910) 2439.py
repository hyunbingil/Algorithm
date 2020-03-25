n = int(input())
star = '*'
blank = ' '
for i in range(n):
    print(blank * (n-(i+1))+star * (i+1))
