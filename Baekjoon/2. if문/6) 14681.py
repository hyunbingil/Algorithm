# 사분면 고르는 문제! x, y 좌표확인해서 몇사분면에 속하는 점인지?
x = int(input())
y = int(input())

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
elif x>0 and y<0:
    print(4)
else:
    print("x 또는 y축 위에 있다.")
                    