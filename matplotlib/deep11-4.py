import matplotlib.pyplot as plt
import numpy as np

# 정규 분포 난수 생성(0.0~1.0)
x = 25 + 6 * np.random.randn(1000)
y1 = 25 + 6 * np.random.randn(1000)
y2 = x + np.random.randn(1000)

# 서브플롯을 추가하기 위한 도식 생성

fig = plt.figure()

# 서브플롯 추가(전체 행, 전체 열, 인덱스)
ax1 = fig.add_subplot(1, 2, 1)	
ax2 = fig.add_subplot(1, 2, 2)

# 서브플롯에 그래프 추가
ax1.scatter(x, y1)			# 산포도 그래프
ax2.scatter(x, y2, color='green')	# 산포도 그래프(녹색)

plt.title("Scatter, 20194146, Lee, Seung Jin")	# 차트 제목
plt.show()		# 맷플롯립 차트 출력
