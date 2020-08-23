user_input = input()
s = ''
storeString = user_input[0]
count = 0
for i in user_input:
    if i == storeString:
        count += 1
    else:
        s += str(count) + storeString
        storeString = i
        count = 1
s += str(count) + storeString
print(s)