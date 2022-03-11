import matplotlib.pyplot as plt
import numpy as np

plt.figure("Numbers (20194146, Lee, Seung Jin)")	# 차트 제목 표시줄 변경
x = np.random.randn(1000)		# 정규 분포 난수 생성(0.0~1.0)
plt.plot(x, marker='o', color='red')	# 선 그래프에 빨간 원형 표식 출력
plt.xlabel("randn()")			# X축 레이블 추가

plt.figure()
plt.title("Numbers (20194146, Lee, Seung Jin)")	# 차트의 속성
x = np.random.rand(1000)		# 난수 생성(0.0~1.0)
plt.plot(x, marker='o', color='red')	# 선 그래프에 빨간 원형 표식 출력
plt.xlabel("rand()")			# X축 레이블 추가

plt.show()		# 맷플롯립 차트 출력
