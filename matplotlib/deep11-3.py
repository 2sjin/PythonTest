import matplotlib.pyplot as plt
import numpy as np

mu = [-10, 0, 10]
sigma = [2, 4, 8]
Gauss = []

plt.figure(figsize=(10,6))	# 차트의 속성(차트 크기=(10, 6))

for i in range(3) :
    Gauss.append(mu[i] + sigma[i] * np.random.randn(10000))	# 정규 분포 난수 생성(0.0~1.0)
    plt.hist(Gauss[i], bins=50, alpha=0.4)	# 히스토그램 생성(데이터, 데이터 구간 수, 투명도)

plt.title("Histogram, 20194146, Lee, Seung Jin")  # 차트 제목

plt.show()  # 맷플롯립 차트 출력
