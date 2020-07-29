number = ''
# arr = []
result = 0
for i in range(1, 101, 1):
    number += str(i)

# 배열에 안담고 문자열로 바로 가능.
# for i in range(0, len(number), 1):
#     arr.append(number[i])

for i in number:
    result += int(i)

print(result)