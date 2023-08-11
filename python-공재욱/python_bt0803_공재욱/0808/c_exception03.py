# 파이썬 예외 처리 방식

#! 1. 모든 예외를 처리하는 방법
# : 모든 에외를 처리하면 예상치못한 오류가 발생할때도 프로그램이 계속 될수있다
# : 가능한 특정 예외를 지정하여 예외 처리
# try - except 문을 사용하여 예외 처리

#* 예외 처리 기본 형태
# try:
#     코드 작성 영역
# except:
#     예외 발생시 처리영역

try:
    a = int(input('정수를 입력하세요.'))
    b = int(input('정수를 입력하세요.'))
    print('{} / {} = {}'.format(a, b, a / b))
except:
    print('예외가 발생 했습니다')

#! 2. 특정 예외만 처리하는 방식

try:
    a = int(input('정수를 입력하세요.'))
    b = int(input('정수를 입력하세요.'))
    print('{} / {} = {}'.format(a, b, a / b))
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')
except ValueError:
    print('정수만 입력할수 있습니다')
except Exception:
    print('기타 오류가 발생 했습니다')

#! 3. 예외 메시지 처리하기
# 모든 예외는 기본적으로 예외 메시지를 내장하고있다
# as키워드를 통해 except문의 예외 메시지를 가지고 올수 있다
