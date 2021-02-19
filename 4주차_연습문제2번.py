#2020010728_허인성
#4주차_연습문제2번
N = int(input())
n = N - 1
m = 1
while n > 0:
    print(" "*n + "*"*m + " "*n)
    n -= 1
    m += 2
while n < N:
    print(" "*n + "*"*m + " "*n)
    n += 1
    m -= 2
