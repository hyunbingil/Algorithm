hamburger_menu = []
drink_menu = []
for i in range(3):
    burger = int(input())
    hamburger_menu.append(burger)

for j in range(2):
    drink = int(input())
    drink_menu.append(drink)

cheap_set = min(hamburger_menu) + min(drink_menu) - 50
print(cheap_set)