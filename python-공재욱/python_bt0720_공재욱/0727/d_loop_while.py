#!
#^ while문: 사용자로부터 숫자를 계속 일벽 받가가
# , 사용자가 0을 입력하면 프로그램이 종료되는 파이썬프로그램을 작성하십시오

while True:
    number = int(input('숫자를 입력해주세요 (0을 입력하면 종료됨니다)  : '))
    if number == 0:
        break