import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# 판다스로 csv 파일 읽기(인코딩 타입 지정)
weather = pd.read_csv('source/weather.csv', encoding='cp949')

weather['month'] = pd.DatetimeIndex(weather['일시']).month	# 특정 레이블의 열만 추출
means = weather.groupby('month').mean()	# 'month' 레이블을 기준으로 데이터 그룹핑 후 평균값 반환
means['평균기온'].plot(kind = 'bar')		# '평균기온' 레이블의 열만 추출하여 막대 그래프 생성

plt.title("20194146 Lee, Seung Jin")	# 차트 제목
plt.show()    # 맷플롯립 차트 출력
