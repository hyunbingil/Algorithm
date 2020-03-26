n = int(input())
a = 0
b = 0
num = 0
m = 0

if not (0 <= n <=99):
    exit()

while True:
    b = n % 10
    a = int(n / 10)
    m = a + b
    c = int(m / 10)
    a = c














    while n != m:
        num = num + 1
        c = int(a) + int(b)
        if c >= 10:
            c = c - 10
        a = c    
        m = str(b)+str(a)
        a = m[0]
        b = m[1]
    print(num)  




if int(n) >= 0 and int(n) < 10:
    a = 0
    b = n[0]
    num = 0
    m = '0'
    num = num + 1
    c = int(a) + int(b)
    a = c    
    m = str(b)+str(a)
    a = m[0]
    b = m[1]
    while True:
        num = num + 1
        c = int(a) + int(b)
        if c >= 10:
            c = c - 10
        a = c    
        m = str(b)+str(a)
        a = m[0]
        b = m[1]
        if n == m:
            break
    print(num)    
elif int(n) >=10 and int(n) <= 99:
    a = n[0]
    b = n[1]
    num = 0
    m = '0'
    while n != m:
        num = num + 1
        c = int(a) + int(b)
        if c >= 10:
            c = c - 10
        a = c    
        m = str(b)+str(a)
        a = m[0]
        b = m[1]
    print(num)   
