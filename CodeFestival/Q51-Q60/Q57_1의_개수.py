one = ''
result = 0

for i in range(0, 1000, 1):
    one += str(i+1)

for i in range(0, len(one), 1):
    if one[i] == '1':
        result += 1

print(result)

# 내장 함수 응용하기
# def count(n):
# 	countN = str(list(range(n+1))).count('1')
# 	return countN

# print(count(1000))