# 1. 어떤수가 양수인지, 음수인지, 아니면 0 인지판단하는 if-else문

num = -5
if num > 0:
    print('양수입니다')
elif num == 0:
    print('0입니다')
else:
    print('음수입니다')



# 2. 1부터 10까지 합을 구하는 프로그램 작성
#    for반복문과 산술 연산자를 사용
# 합개를 저장할 변수를 0 으로 초기화 합니다
total = 0
# 1부터 10 까지의 보든 정수를 순회(반복)하면서 합계를 업데이트 합니다
for i in range(1, 11):
    total += i # total + i

# 최종합계를 출력합니다
print('thr sum from 1 to 10 is', total)