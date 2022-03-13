print("20194146 이승진")

import pandas as pd

# 판다스로 csv 파일 읽기(0열을 인덱스로 사용)
countries_df = pd.read_csv('data/countries.csv', index_col = 0)

# 데이터 정렬('area' 기준, 내림차순)
sorted = countries_df.sort_values('area', ascending = False)

# 처음 5행의 데이터 출력
print(sorted.head())
