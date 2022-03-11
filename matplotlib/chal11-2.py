import matplotlib.pyplot as plt

plt.title("20194146, Lee, Seung Jin")	# 차트 제목

x = [x/10 for x in range(20)]
y1 = [(x/10)**2 for x in range(20)]
y2 = [(x/10)**3 for x in range(20)]
y3 = [2**(x/10) for x in range(20)]

# 선 그래프(x값, y값, 레이블)
plt.plot(x, x, label='linear')
plt.plot(x, y1, label='quadratic')
plt.plot(x, y2, label='qubic')
plt.plot(x, y3, label='power')

plt.xlabel("x label")	# X축 레이블 추가
plt.ylabel("y label")	# Y축 레이블 추가
plt.legend()	# 범례 추가(모든 레이블 출력)

plt.show()		# 맷플롯립 차트 출력

