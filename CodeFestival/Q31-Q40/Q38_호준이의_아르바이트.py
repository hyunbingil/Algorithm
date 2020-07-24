scores = list(map(int, input().split(" ")))
dupli = list(set(scores))
dupli.sort(reverse=True)
dupli = dupli[0:3]

c = scores.count(dupli[0]) + scores.count(dupli[1]) + scores.count(dupli[2])
print(c)

# user_input = input()

# l = list(user_input.strip().split())
# l = [int (i) for i in l]

# count = 3
# #3개는 무조건 구매, 배열 정렬 후 1~3위 중 중복되는 숫자까지 포함

# data_sorted = sorted(list(l))

# print(data_sorted)
# for i in range(len(l)-1, 0, -1):
# 	if data_sorted[-3] == l[i]:
# 		count += 1
# print(count)