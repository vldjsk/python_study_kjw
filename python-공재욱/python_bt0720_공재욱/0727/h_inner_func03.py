### 시퀀스 내장 함수 ###

# 시퀀스 자료현: 요소들이 연속적으로 이루어진 자료형
# 리스트, 튜플 문자열 등

# 1. enumerate() 함수 - 리스트
# 리스트에 저장된 요소와 해당 요소의 인덱스다 튜플 형태로 함께 추출

# for item in enumerate([리스트])
#     반복 실행문

for item in enumerate(['가위', '바위', '보']):
    print(item)
# (0, '가위') # 인덱스 번호, 요소값
# (1, '바위')
# (2, '보')

# 2. range() 함수
# 숫자 리스트를 생성하는데 사용
# 주로 for 반복문에서 사용, 일정한 간격의 숫자 시퀀스 생성 가능

#range(stop): 0부터 stop 1 까지의 정수를 반환
for i in range(5):
    print(i)

# range(start, stop): start ~ stop -1
for i in range(1, 5)
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2)
    print(i)

# 3. ien() 함수
# 컨테이너에 있는 원소늬 개수를 반환
# 리스트, 튜플, 문쟈열, 딕셔너리

my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # 5

my_string = "hello python"
print(len(my_string)) # 15

# sorted() 함수
#리스트를 정렬하여 반환 (기본: 오름차순 정렬)
# 내림차순 정렬: reverse-True 설정
my_list = [5, 1, ]