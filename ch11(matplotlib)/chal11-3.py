import math
import matplotlib.pyplot as plt

plt.title("SINE & COSIZE WAVE, 20194146, Lee, Seung Jin")	# 차트 제목

x = []
y = []
z = []

for angle in range(360) :
    x.append(angle)	# 각도(0~360) 저장
    y.append(math.sin(math.radians(angle)))	# 각도에 따른 사인함수 값 저장
    z.append(math.cos(math.radians(angle)))	# 각도에 따른 코사인함수 값 저장

plt.plot(x, y, color = 'blue')	# (x, y) 선 그래프: 파랑색 실선
plt.plot(x, z, color = 'red')	# (x, z) 선 그래프: 빨강색 실선

plt.show()		# 맷플롯립 차트 출력


