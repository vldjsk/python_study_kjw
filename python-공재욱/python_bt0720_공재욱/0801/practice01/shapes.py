### 정사각형과 원의 넓이를 계산하는 함수 모듈 ###
# 1. calculate_square_area 함수 (정사각형의 넓이)
# 한변의 길이를 인자로 받아 정사각형 넓이를 반환
import math


def calculate_square_area(a):
    return a * a


# 2. calculate_circle_area함수 (원의 넓이)
# 반지름을 받아 원의 넓이를 반환
# 반지름 * 반지름* 3.14
def calculate_circle_area(b):
    return b * b * math.pi