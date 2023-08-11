### 파이썬 모듈 ###

# 1. 모듈의 정의
# : 함수나 변수 또는 클래스를 모아놓은 파이썬 파일

# 2. 모듈의 필요성
# 2-1. 코드의 재사용성
# : 모듈은 한변 작성하면 계속해서 재사용이 가능
# : 개발시간 단축 & 코드의 일관성 유지 용이

# 2-2. 코드의 구조화
# : 코드의 유지보수 용이 & 코드의 이해도가 높아짐

# 3. 파이썬 모듈 사용방법
# import 키워드를 사용하여 '불러오기'가 가능
# import 할때에는 .py 생략하여 파일명민 작성

# b-my-modul를 불러와서 사용하기
import b_my_module

print(b_my_module.add(3, 5))
print(b_my_module.sub(4, 2))

# 3-2. from import 사용
# from 모듈명 import 항목명
# : 특정 모듈에서 하나이상의 특정 항목만 불러오기 가능
# : 항목을 사용할때 모둘령을 접두어로 붙이지 않아도 가능

# 여러항목을 동시에 불러오는 경우 쉼표(,)를 사용하여 나열 가능

from  b_my_module import info, greet

print(greet('공재욱'))
print(info(50))

# 3-3. import as 사용
# : 모듈의 이름이 길거나 다른모듈과 충돌할 가능성이 있는경우
# : 모듈에 대한별칭(aliae)를 지정하는것이 유용
# as 키워드를 사용하여 별칭 지정 가능

import b_my_module as mm

print(mm.add(5, 7))
print(mm.sub(5, 7))

from b_my_module import greet as hello
# b-my-module모듈 안에 greet항목을 hello 별칭으로 사용

print(hello('공재욱'))