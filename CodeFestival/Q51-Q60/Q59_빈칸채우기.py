n = input()
real = (50 - len(n))

for i in range(0, int(real/2)):
    print("=", end="")
print(n, end="")

for i in range(0, int(real/2)):
    print("=", end="")

# user_input = input()
# print("{0:=^50}".format(user_input))    