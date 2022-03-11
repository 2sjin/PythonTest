import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# 판다스로 csv 파일 읽기(인코딩 타입 지정)
weather = pd.read_csv('source/weather.csv', encoding='cp949')

monthly = [ None for x in range(12) ]
monthly_wind = [ 0 for x in range(12) ]

# '일시' 레이블의 열만 추출하고 연산하여 새로운 ‘month’ 레이블에 추가
weather['month'] = pd.DatetimeIndex(weather['일시']).month

for i in range(12) :
    # 특정 레이블의 열만 추출
    monthly[i] = weather[weather['month'] == i + 1]
    monthly_wind[i] = monthly[i].mean()['평균기온']

plt.plot(monthly_wind, 'red')			# 빨간 직선 그래프 생성
plt.xticks(range(12), range(1, 13))		# X축 눈금 설정(눈금 인덱스, 눈금 표시 값)
plt.title("20194146 Lee, Seung Jin")	# 차트 제목
plt.show()		# 맷플롯립 차트 출력
