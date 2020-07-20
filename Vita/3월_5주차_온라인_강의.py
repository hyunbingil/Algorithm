# (★1)
""" 
<문제>
최근 코로나 바이러스의 여파로 다양한 교육기관에서 온라인 강의를 통해 교육을 진행하고 있다.
하지만 온라인 강의를 틀어놓고 다른 행동을 하거나 자러가는 학생들이 생겨, 이를 잡아내기 위해 새로운 시스템을 도입하였다.
기존에는 강의 시간보다 미달되는 경우에 한해 출석을 인정하지 않았지만, 이제는 강의 시간보다 10분 이상 수강한 경우에도 출석을 인정하지 않도록 시스템을 수정하였다.
전체 강의 시간과 학생이 수강한 강의 시간이 주어졌을 때, 출석으로 인정받을 수 있는지 확인해보자!
"""

"""
<입력>
전체 강의 시간과 학생이 수강한 강의 시간이 한 줄에 하나씩 HH : MM의 형태로 주어진다.
"""

"""
<출력>
학생이 수강한 강의 시간에 따라 출석으로 인정받을 수 있다면 1, 없다면 0을 출력한다.
"""

lec_h, lec_m = input().split(':')
att_h, att_m = input().split(':')

lec_m = int(lec_m)
lec_h = int(lec_h) * 60

att_m = int(att_m)
att_h = int(att_h) * 60

lec_time = lec_h + lec_m
att_time = att_h + att_m

if lec_time - att_time >= 10:
    print(0)
elif att_time - lec_time >= 10:
    print(0)
else:
    print(1)        