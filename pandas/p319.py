print("20194146 이승진")

import pandas as pd

# 판다스로 csv 파일 읽기(0열을 인덱스로 사용)
countries_df = pd.read_csv('data/countries.csv', index_col = 0)

# 특정 레이블의 열만 추출하고 연산하여 새로운 ‘destiny’ 레이블에 추가
countries_df['destiny'] = countries_df['population'] / countries_df['area']

# 행을 슬라이싱하여 데이터 출력
print(countries_df[0:7])


