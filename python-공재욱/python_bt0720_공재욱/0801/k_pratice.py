### 모듈 실습 문제 ###`
# p.221

# 파이썬으로 자동으로 실행되는 로또 추첨 프로그램을 다음 지시사항에 따라 구현하세요
import random
import time
pot = list(range(1, 46))
jacpot = []
# for반복문에서 _(언더바 사용 시 특별히 사용 되지 않는 변수)
for _ in range(6):
    random.shuffle(pot)
    jacpot.append(pot.pop())
    time.sleep(2/6)
jacpot.sort()
print(jacpot)

