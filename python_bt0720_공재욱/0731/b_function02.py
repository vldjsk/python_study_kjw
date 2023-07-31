### 매개변수 ###

# 1. 매개 변수의 정의
# : 함수가 호출될때 함수에 전달되는 것들을 받아내는 역할
def greet(name):
    print(f'hello, {name}!')

greet('공재욱') # '공재욱': 변수

# 2. 위치 매개변수: 함수를 호출할때 전달된 인수의 순서대로 매개면수에 대입
def info(name, age):
    print(f'I am {name} and I am {age} years old')

info('dk', 50)

# 3. 기본(디폴트 default) 매개변수

def greet(name = 'python'):
    print(f'hello {name}')

greet('나')
greet()

