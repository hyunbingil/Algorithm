def one(n):
    def two(m):
        mul = m
        for i in range(0, n-1, 1):
            m = m * mul
        return m    
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))

# ** 사용하면 제곱 가능

# def one(n):
#     def two(value):
#         sq = value ** n
#         return sq
#     return two

# a = one(2)
# b = one(3)
# c = one(4)
# print(a(10))
# print(b(10))
# print(c(10))