# 가변 인자(매개변수)를 받아 평균을 반환하는 함수를 작성
# sum() len() 내장함수 사용
def average(*args):
    return sum(args) / len(args)

print(average(1, 2, 3, 4, 5)) # 15 / 5 -3.0