test = []
for i in range(5):
    score = int(input())
    if score >=40:
        test.append(score)
    else:
        test.append(40)
        
print(round(sum(test)/5))