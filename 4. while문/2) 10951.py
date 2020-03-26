import sys
# sys 모듈에 대해서 study repository에 정리해뒀으니 참고!
for line in sys.stdin:
    a, b = map(int,line.split())
    print(a+b)
