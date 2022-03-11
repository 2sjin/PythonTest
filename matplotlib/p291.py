import matplotlib.pyplot as plt
import numpy as np

plt.title("GDP per capita, 20194146, Lee, Seung Jin")	# 차트 제목

years = [1965, 1975, 1985, 1995, 2005, 2015]
ko = [130, 650, 2450, 11600, 17790, 27250]
jp = [800, 5120, 11500, 42130, 40560, 38780]
ch = [100, 200, 290, 540, 1760, 7940]

# 정수 범위에 해당하는 넘파이 배열 생성(range() 함수와 유사함)
x_range = np.arange(len(years))

# 막대 그래프(x값+출력보정값, y값, 막대의 두께)
plt.bar(x_range + 0.0, ko, width = 0.25)
plt.bar(x_range + 0.3, jp, width = 0.25)
plt.bar(x_range + 0.6, ch, width = 0.25)

plt.xticks(range(len(years)), years)	# X축 눈금 설정(눈금 인덱스, 눈금 표시 값)
plt.xlabel("years")		# X축 레이블 추가
plt.ylabel("dollars")		# Y축 레이블 추가

plt.show()		# 맷플롯립 차트 출력
