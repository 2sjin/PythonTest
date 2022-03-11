import pandas as pd
import matplotlib.pyplot as plt

# 판다스로 csv 파일 읽기(0열을 인덱스로 사용)
countries_df = pd.read_csv('data/countries.csv', index_col = 0)	

# 마지막 5행의 데이터만 저장
countries_df = countries_df.tail()

# 'population' 레이블의 열만 추출하여 막대 그래프 생성
plt.figure()	# 새 창 만들기
countries_df['population'].plot(kind='bar', color=('b', 'darkorange', 'g', 'r', 'm'))

# 'population' 레이블의 열만 추출하여 원 그래프 생성(새 창)
plt.figure()	# 새 창 만들기
countries_df['population'].plot(kind='pie')

plt.show()		# 맷플롯립 차트 출력
