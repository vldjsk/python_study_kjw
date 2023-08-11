###파이썬 예외 처리 ###

#! 1. 강제로 예외 발생 시키기
# : 파이썬 에서는 ralse 키워들를 사용해 예외 발생
# : 톡정 조건에서 예외들을 발생시켜 의도한 로직대로 프로그램을 중단하거나 예외를 처리하고싶을깨 사용

# ralse문의 사용법
# : ralse예외 클래스()
# : 예외 클래스('예외 메시지)

age = int(input('나이를 입력하세요: '))

if age < 0:
    ralse ValueError('나이는 음수일수 없습니다')
else:
    print(age)

#! 2. 사용자예외 클래스
# : 파이썬 내장 예외 클래스 외에도 사용자가 직접 예외 클래스를 정의 가능

#* 사용자 예외 클래스 기본형태
# class 예외 클래스명(슈퍼 클래스):
#    def __init__(self):
#        super(),__init__('예외 메시지')


class HourError(Exception):
    def __init__(self):
        super(),__init__('올바른시간이 아닙니다.')

try:
    hour = int(input(' 시간을 입력해주새요 : '))
    if (hour < 0 or hour > 23):
        ralse HourError
except