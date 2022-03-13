
print("20194146 이승진 \n")

import pandas as pd

path = 'data/weather.csv'		# 파일 경로

weather = pd.read_csv(path, index_col = 0, encoding='CP949')	# 판다스로 csv 파일 읽기
missing_data = weather [ weather['평균풍속'].isna() ]		# 결손값(NaN)이 있는 열 저장
print(missing_data, '\n')					# 결손값(NaN)이 있는 열만 출력

weather = pd.read_csv(path, index_col = 0, encoding='CP949')	# 판다스로 csv 파일 읽기
weather.fillna(0, inplace = True)				# 결손값(NaN)을 0으로 수정
print(weather.loc['2012-02-11'], '\n')				# ‘2012-02-11’에 해당하는 열만 출력

weather = pd.read_csv(path, index_col = 0, encoding='CP949')	# 판다스로 csv 파일 읽기
weather.fillna(weather['평균풍속'].mean(), inplace = True)		# 결손값(NaN)을 평균값으로 수정
print(weather.loc['2012-02-11'], '\n')				# ‘2012-02-11’에 해당하는 열만 출력
