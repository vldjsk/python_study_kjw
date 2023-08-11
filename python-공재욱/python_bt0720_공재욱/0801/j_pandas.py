### 파이썬 오부 모듈 - pqndas ###

# pandas
# : python data analysis library의 약자
# : 파이썬 에서는 데이터 분석을 위해 사용되는 라이브러리

# pandas dataframe 생성
# : 여러개의 컬럼으로 구성된 2차원의 네이터 구조

import pandas as pd

#dataframe 생성
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c']
})

# 데이터 엑세스: 특징 데이터에 접근

# column에 접근 (세로)
print(df['A'])
# A읜 값을 인덱스 번호로 나누어 측정

# row에 접근 (가로)
#Dataframe명.loc(인덱스 번호)
# 인덱스 번호의 데이터를 출력
print(df.loc[1])