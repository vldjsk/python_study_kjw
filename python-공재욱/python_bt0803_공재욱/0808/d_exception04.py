### else문과 fainally문 ###

#! else문
# : try 블록에서 예외가 발생하지않으면 처리되는 구문
# : 주로 정상적으로 코드가 장상적으로 실행되는 경우 수행할 작업 정의

#! finally문
# : 예외 발생과 상관 없이 항상 처리되는 구문
# : 주로 파일 닫기 등과 같은 필수적인작업을 정의

# try:
#     코드 작성 영역
# except:
#     예외 발생시 처리령역
# else:
#     예외가 없을 때 처리 영역
# finally:
#     언제나 실행되는 영역

#! 3. else문 예제
try:
    number = int(input('정수를 입력하세요.'))
except ValueError as e:
    print(e)
else:
    print(f"입력한숫자는 {number}입니다")
finally:
    print('프로그램을 종료합니다')

#! 4. finally문 예제
file = open('D:\python-공재욱\python_bt0803_공재욱\0808\file.txt', 'r', encoding=)