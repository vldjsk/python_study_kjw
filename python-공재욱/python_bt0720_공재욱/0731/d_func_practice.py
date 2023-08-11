def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devide(a, b):
    return a / b
# 조건문을 사용해서 b가 0일경우 "Error: cannot divide by Zero
# 0 이 아닐경우에는 a / b
def devide(a, b):
    if b == 0:
        return "Error: cannot divide by Zero"
    else:
        return a / b

# 4개의 함수 호출
print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(devide(10, 5))
# print(devide(10, 0)) # Error: ZeroDivisionError: division by zero