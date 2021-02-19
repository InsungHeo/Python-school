#2020010728_허인성
#2주차_연습문제3번

sec = int(input('시간을 "초"단위로 입력하세요:    '))
hr = sec//3600
m = (sec - 3600*hr)//60
s = sec%60
print(str(sec) + '초는 ' + str(hr) + '시간, ' + str(m) + '분, ' + str(s) + '초입니다.')
