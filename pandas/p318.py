print("20194146 이승진 \n")

import pandas as pd

# 판다스로 csv 파일 읽기(0열을 인덱스로 사용)
df = pd.read_csv('data/countries.csv', index_col = 0)

# 처음 5행의 데이터 출력
print(df.head(), "\n")

# 마지막 5행의 데이터 출력
print(df.tail(), "\n")

# 행을 슬라이싱하여 데이터 출력
print(df[3:6], "\n")
