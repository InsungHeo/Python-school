#융합전자공학부 2020010728 허인성
def substring(a): #숫자문자열의 하위문자열 리스트가 집합 Sk의 원소이면 True 반환
    cnt = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            if int(a[i:j]) % len(a) == 0:
                cnt += 1
            if cnt == 2:
                return False
    if cnt == 1:
        return True

def F(N): #N보다 작은 숫자들 중 집합 Sk에 속하는 원소의 개수
    cnt = 0
    S=[]
    for i in range(1, N):
        if substring(str(i)):
            if N<100:
                S.append(i)
            cnt += 1
            
    print('F(' + str(N) + ')','=', cnt)
    if N<100:
        print(S)

print("융합전자공학부 2020010728 허인성 10/30에 제출합니다.\n")

print('\n1. F(6)의 값고 Sk의 원소를 오름차순으로 모두 출력')
F(6)

print('\n2. F(10)를 만족하는 Sk의 원소를 오름차순으로 모두 출력')
F(10)

print('\n3. F(100,000)과 F(1000,000,000)을 계산하여 화면에 출력')
F(100000)
F(1000000000)


