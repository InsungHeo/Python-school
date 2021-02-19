#2020010728_허인성
#3주차_연습문제1번
a = int(input('첫 번째 정수를 입력하시오:  '))
b = int(input('첫 번째 정수를 입력하시오:  '))
if a == b:
    print('두 수는 같습니다.')
elif a < b:
    print('큰 수: ' + str(b))
    print('작은 수: ' + str(a))
else:
    print('큰 수: ' + str(a))
    print('작은 수: ' + str(b))
