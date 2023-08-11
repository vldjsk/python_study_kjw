### 예외 처리 ###

# 1. if문(고전적인 예외 처리 방법)
a = int(input('정수를 입력하세요.'))
b = int(input('정수를 입력하세요.'))

# a / b
if b == 0:
    print('0으로 나눌 수 없습니다')
# b에 0값이 들어올 경우 
else:
    print('{} / {} = {}'.format(a, b, a / b))

num1 = 5
num2 = 3
print(num1 + num2)

# 고전적인if 조건문 예외 처리 경우
# 코드 벅잡성 증가, 가독성 저하, 예상치 못한 에러 처리의 어려움이 존제

#! 2. 예외의 종류

# 2-1. 내장 예외의 종류
# baseException: 죄상위 클래스
# ValueError: 잘못된 값이 입력될때 발생
