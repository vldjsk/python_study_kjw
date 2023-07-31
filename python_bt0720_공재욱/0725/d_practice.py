# 연산자 복습문제 #

# 1. 임의의 두자리수 정수(10 ~ 99)를 입력 받아서
# 십의 자리와 일의 다리로 분리하여 출력하는 프로그램 구현

number = int(input('두 자리 정수를 입력해 주세요(10 ~ 99) : '))
tens = number // 10
ones = number % 10
print('십의 자리 : ', tens)
print('일의 자리 : ', ones)

# 2. 임의의 세 자리 정수 (100 ~ 999)를 입력 받아서
# 백의 자리, 십의 자리, 일의 자리로 분리하여 출력하는 프로그램을 작성 하세요

number = int(input('세 자리 정수를 입력해주세요(100 ~ 999) : '))
hundreds = number//100
tens = (number % 100) // 10
ones = number % 10

print('백의 자리 : ', hundreds)
print('십의 자리 : ', tens)
print('일의 자리 : ', ones)

# 3. 1분은 60초이고 1시간은 60분입니다. 따라서1시간은 3600초 입니다
# 임의의 초를 입력받아 해당 초를 시, 분, 초로 변환하여 출력하는 프로그램을 구연해 주세요

# 입력받은 초를 담는 변수 total_seconds

# hours, minutes, seconds

# 초를 입력받습니다.
total_seconds = int(input('초를 입력해주세요'))

# 입력받은 초를 시, 분, 초로 변환합니다.
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
second = total_seconds % 60

# 결과를 출력합니다
print(f"{total_seconds}초는 {hours}시간 {minutes}분 {second}초 입니다")