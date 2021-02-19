#2020010728_허인성
#4주차_연습문제2번
print("숫자를 입력하세요.")
s = 0
a = 0
m = 0
M = 0
c = 0
while True:
    x = input()
    if x == "입력 끝" :
        break
    else :
        x = int(x)
    if c == 0:
        M = x
        m = x

    s += x

    if M < x:
         M = x
    if m > x:
         m =x
    c += 1

a = s/c
print("입력받은 숫자들의 합은 " + str(s))
print("입력받은 숫자들의 평균은 " + str(a))
print("가장 큰 숫자는 " + str(M))
print("가장 작은 숫자는 " + str(m))
