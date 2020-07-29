# 내 답 : 문자열 사용
s = input()
result = ''
for i in s:
    if i.isupper() == True:
        result += i.lower()
    else:
        result += i.upper()

print(result)

# 답안 : 배열 사용
# a = input()
# b = []

# for i in a:
# 	if i.islower():
# 		b.append(i.upper())
# 	else:
# 		b.append(i.lower())
	
# for i in b:
# 	print(i, end='')