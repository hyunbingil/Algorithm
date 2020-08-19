all = [] ; x=1;y=1
for i in range(10):
    a = list(map(int,input().split()))
    all.append(a)
while(True) :
    if all[x][y] == 2 : #먹이 발견했을때 break
        all[x][y] = 9
        break
    elif all[x+1][y] ==1 and all[x][y+1] ==1 :  #벽으로 가로 막혔을때 break
        all[x][y] = 9
        break
    all[x][y] = 9
    if all[x][y+1] == 1 :  #오른쪽이 벽이면 아래로 1칸
        x +=1
    elif all[x+1][y] == 1 :  # 아래쪽이 벽이면 오른쪽으로 1칸
        y += 1
    else : y+=1 # 주변에 벽이 없으면 오른쪽으로 1칸
for p in all :
    for o in p:
        print(o,end=" ")
    print()