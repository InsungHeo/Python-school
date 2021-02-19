#2020010728_허인성
#7주차_연습문제1번

"""
입력되는 수의 제한이 없도록 프로그램을 작성할 것
for-in을 사용하여 검사 방식을 줄일 것
"""

def a(n):
    c = 0
    print(n, "->", end = "  ")
    for i in n:
        for j in '369':
            if i == j:
                print('clap!', end = " ")
                c = 1
    if c == 1:
        print()
    if c == 0:
        print(n)

print("Shout the number sequentially from 1 to the last number.")
print("When 3 or 6 or 9, clap, nstead of shouting.")
print("Enjoy the game!")
n = int(input("Please input the number."))
l = list(range(1, n+1))
for i in range(n):
    l[i] = str(l[i])
m = 1
while m <= n:
    a(str(m))
    m += 1
