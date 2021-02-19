#2020010728_허인성
#6주차_연습문제1-2번

import random as r
import time as t


def chooseInput():
    c = rsp[r.randint(0, 2)]
    p = input("\n\n 가위~ 바위~ 보~          ")
    return [p, c]
def decideWinner(p, c):
    print("두구둑두구두구~\n")
    t.sleep(1)
    print("\ncomputer: ", c, ' player: ', p)
    if c == p:
        return 0

    if c == '가위':
        if p == '바위':
            return 'player'
        if p == '보':
            return 'computer'

    if c == '바위':
        if p == '보':
            return 'player'
        if p == '가위':
            return 'computer'

    if c == '보':
        if p == '가위':
            return 'player'
        if p == '바위':
            return 'computer'

    
print("지금부터 이기기 전까지 끝나지 않는 가위바위보 게임을 시작하지.")
rsp = ['가위', '바위', '보']
win = 0

while True:
    a = chooseInput()
    winner = decideWinner(a[0], a[1])

    if winner == 'player':
        print('승리!')
        break
    elif winner == 'computer':
        print('패배..')
    else :
        print('무승부')
