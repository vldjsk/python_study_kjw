# 연산자(operator)
# : 특정 작업을 수행하는데 사용되는 특수기호나 구문

# 항목의 개수: 단항, 이항, 삼항 연산자로 구분
# 사용 목적: 산술, 대입, 관계, 논리 연산자로 구분

# 파일(폴더)명 변경 단축기 : shift + F6

### 산술 연산자 ###

# 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/)
# 모듈로(%), 제곱(**), 몫(//)

a = 5
b = 3
print(a + b) # 덧셈: 8
print(a - b) # 뻴셈: 2
print(a * b) # 곱셈:15
print(a / b) # 나눗셈: 1.666666666666666
print(a % b) # 모듈로(어떤 한 숫자를 다른 숫자로 나눈 나머지를 구하는 연산): 2
print(a ** b) # 제곱: 5 * 5 * 5 = 125
print(a // b) # 몫: 1

### 비교 연산자 ##
# 결과 값이 boolean타입으로 변화
# 두값이 같은지(==), 두값이 같지 않은지(!=)
# 이상(>=), 이하(<=), 초과(>), 미만(<)

a = 10
b = 20
print(a == b) # False
print(a != b) # True
print(a >= b) # False
print(a <= b) # True
print(a < b) # True
print(a > b) #False

### 할당 연산자
# : 변수에 값을 할당하는데 사용
# 기본 할당 연산자: 등호(=)
# 복합 할당 연산자: +=, -=, *=, /=, %=, **=, //=

a = 10 # 10을 a에 할당

a += 5 # a = a + 5와 동일 (a의 값: 15)
a -= 2 # a = a - 2와 동일 (a의 값: 13)
a *= 2 # a = a * 2와 동일 (a의 값: 26)
a /= 2 # a = a / 2와 동일 (a의 값: 13.0)

print(a)

### 논리 연산자 ###
# : boolean값(Ture, False)아르 다루는 연산자
# : and, or, not

a = True
b = False
print(a and b) #False
# : and 연산자는 모든 조건이 Ture일때 Ture를 반환
# : 그렇지 않으면 False를 반환

print(a or b)
# : or 연산자는 적어도 하나의 조건이 Ture 일 떄 Ture를 변환
# : 모든 조건이 False일 때만 False를 반환

print(not a) # False
# not 연산자는 boolean값을 반환

print('======================================================')

# 변수 'a'와 'b'에 각각 10과 5를 할당하고, 그 합을 변수 'c'에 저장한 후 출력하세요.
a = 10
b = 5
c = a + b
print(c)

# 변수 'd'에 7을 할당하고, 변수 'd'의 값에 3을 더한 후 다시 'd'에 저장하고 출력하세요.
d = 7
d += 3
print(d)

# 두 숫자가 모두 10보다 크거나 같은지 확인하는 코드를 작성하세요. 변수 'e'와 'f'에는 각각 12와 9를 할당합니다.
e = 12
f = 9
print(e >= 10 and f >= 10)

# 변수 'g'에 True를 할당하고, 'g'의 불리언 값을 반전시킨 후 출력하세요.
g = True
print(not g)

