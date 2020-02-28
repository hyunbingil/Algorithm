# 빠르게 A+B를 여러번 출력하는 문제
import sys
# sys.stdin.readline() 사용해서 푸는 문제.
# 뭔지 몰라서 찾아봤음ㅋㅋ.ㅋ.ㅋ.ㅋㅋ

t = int(input())

for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
