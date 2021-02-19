#2020010728_허인성
#6주차_연습문제1-1번

import random as r
import time as t

print("지금부터 이기기 전까지 끝나지 않는 가위바위보 게임을 시작하지.")
rsp = ['가위', '바위', '보']
win = 0

while True:
    c = rsp[r.randint(0, 2)]
    p = input("\n\n 가위~ 바위~ 보~          ")
    print("두구둑두구두구~\n")
    t.sleep(1)
    if c == p:
        print("무승부", "\ncomputer: ", c, ' player: ', p)

    if c == '가위':
        if p == '바위':
            print("승리!", "\ncomputer: ", c, ' player: ', p)
            win = 1
        if p == '보':
            print("패배..", "\ncomputer: ", c, ' player: ', p)

    if c == '바위':
        if p == '보':
            print("승리!", "\ncomputer: ", c, ' player: ', p)
            win = 1
        if p == '가위':
            print("패배..", "\ncomputer: ", c, ' player: ', p)

    if c == '보':
        if p == '가위':
            print("승리!", "\ncomputer: ", c, ' player: ', p)
            win = 1
        if p == '바위':
            print("패배..", "\ncomputer: ", c, ' player: ', p)
    if win == 1:
        break
