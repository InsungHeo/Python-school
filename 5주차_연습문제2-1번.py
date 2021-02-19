#2020010728_허인성
#5주차_연습문제2-1번

"""
- 1부터 45까지 정수 중에 6개를 무작위로 선택
- 6개의 숫자는 모두 달라야함
- del 이용
"""
import random as r
roddo = list(range(1, 46))
c = 0
x = 0
while c < 6:
    x = r.randint(0, 44 - c)
    c += 1
    print(roddo[x], end = " ")
    del roddo[x]
