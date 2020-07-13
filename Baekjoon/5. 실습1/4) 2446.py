n = int(input())
star = '*'
real = n
blank = ' '
for k in range(n):
    print((blank * int(((2*n-1)-(2*real-1))/2))+(star * (2*real-1)))
    real = n - (k+1)
real = 1    
for i in range(1,n):
    real = real + 1
    print(blank * int(((2*n-1)-(2*real-1))/2)+(star * (2*real-1)))