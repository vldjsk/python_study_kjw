### 지역 변수& 전역 변수 ###

# 지역(local) 변수
# : 특정함수 또는  매서드 내부에서 선언된변수
# : 선언된 함수 또는 매서드 내에서만 접근 가능
# : 함수가 종료되면 그 생명 주기도 끝남

def my_func():
    local_var = "I'm a local variable"
    print(local_var)

my_func()
# print(local_var) # Erroe: 'local_var' is not defined


# 전역(global) 변수
# : 함수 외부에서 선언되며 프로그램에서 접근할수있는 변수
# : 함수내부에서 전역 변수를 사용하려면 global 키워드를 사용하여 선언

global_var = "I;m a global variable"

def my_func2():


