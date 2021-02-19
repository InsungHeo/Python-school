#2020010728_허인성
#6주차_연습문제2번

import random as r
import time as t


def chooseInput():
    c1 = rsp[r.randint(0, 2)]
    c2 = rsp[r.randint(0, 2)]
    return [c1, c2]
  
def decideWinner(c1, c2):
    if c1 == c2:
        return 0

    if c1 == '가위':
        if c2 == '바위':
            return 'computer2'
        if c2 == '보':
            return 'computer1'

    if c1 == '바위':
        if c2 == '보':
            return 'computer2'
        if c2 == '가위':
            return 'computer1'

    if c1 == '보':
        if c2 == '가위':
            return 'computer2'
        if c2 == '바위':
            return 'computer1'
    
print("흥미진진한 컴퓨터들의 가위바위보 대결을 감상해보도록 하지,")
rsp = ['가위', '바위', '보']
win = 0
draw = 0
lose = 0
n = int(input("몇 번의 대결의 결과를 확인하시겠습니까?        "))
for _ in range(n):
    a = chooseInput()
    winner = decideWinner(a[0], a[1])

    if winner == 'computer2':
        print('computer2의 승리\n')
        lose += 1
    elif winner == 'computer1':
        print('computer1의 승리\n')
        win += 1
    else :
        print('무승부\n')
        draw += 1
print("computer1 기준 ", n, "전 ", win, "승 ", lose, "패 ", draw, "무 ")
print(win/n*100, "%")
