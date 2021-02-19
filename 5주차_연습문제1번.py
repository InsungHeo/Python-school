#2020010728_허인성
#5주차_연습문제1번

"""
while과 append()를 이용하여 다음을 출력하시오.
- 1부터 100까지 숫자가 저장된 리스트 만들기
- 1부터 100까지 숫자 중 짝수가 저장된 리스트 만들기
"""

l1 = []
l2 = []
c = 1
d = 2
while c < 101:
    l1.append(c)
    c += 1
while d < 101:
    l2.append(d)
    d += 2
print(l1)
print()
print(l2)
