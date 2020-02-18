h, m = input().split()
h = int(h)
m = int(m)
if m<45 and h>=1:
    h=h-1
    m = m+15
elif m>=45:
    m = m-45    
else:
    h = 23
    m = m+15

print(h, m, sep = " ")    

# 24시간으로 계산하기 때문에 23와 1시 이때 경우도 적어줘야합니다.^^..