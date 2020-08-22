student = ['강은지','김유정','박현서','최성훈','홍유진','박지호','권윤일','김채리','한지호','김진이','김민호','강채연']
student.sort()
for i in range(0, len(student)):
    print("번호: %d, " % (i+1), end="")
    print("이름: %s" % student[i])