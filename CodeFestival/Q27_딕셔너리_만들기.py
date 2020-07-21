keys = input().split()
scores = map(int, input().split())

dic = dict(zip(keys, scores))
print(dic)

# zip은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수.