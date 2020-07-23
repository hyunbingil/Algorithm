import copy
height = list(input().split())
tmp = copy.deepcopy(height)
height.sort()
' '.join(tmp)
' '.join(height)

if tmp == height:
    print("YES")
else:
    print("NO")    



# user_input = input()

# l = list(user_input.strip().split())
# l = [int (i) for i in l]

# if l != sorted(l):
# 	print("NO")
	
# else:
# 	print("YES")