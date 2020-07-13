# 풀이1)
a,b,c = map(int, input().split()) # 하나하나 int로 바꾸기 귀찮아서 쓴 친구.
maxx = max(a,b,c)
minn = min(a,b,c)
print(a+b+c - maxx - minn)

# 풀이2)
a = map(int, input().split())
b = sorted(a)
print(b[1])

""" if (a > b and a > c):
    #max = a
    #if(b > c):
        #secmax = b
    else:
        secmax = c
elif (b > a and b > c):
    max = b
    if(a > c):
        secmax = a
    else:
        secmax = c    
elif (c > a and c > b):
    max = c
    if(a > b):
        secmax = a
    else:
        secmax = b    
elif (a = b and a > c):
    max = a
    secmax = c
elif (a = c and ) ...
잠시만 이렇게 노가다해야한다고..?
파이썬에는 뭔가 이런 값 알려주는
내장함수나 정렬해주는거 있을거같은데... 찾아봐야지....."""

