import matplotlib.pyplot as plt

plt.title("20194146, Lee, Seung Jin")	# 차트 제목

x = [x for x in range(-20, 20)]
y1 = [t**2 + 2*t + 1 for t in x]	# 
y2 = [t**2 - 20 for t in x]		# 
y3 = [5*t + 5 for t in x]		# 

# (x, y1) 선 그래프: 빨강색 점선
# (x, y2) 선 그래프: 삼각형 표식의 녹색 실선
# (x, y3) 선 그래프: 별표 표시식 파랑색 짧은 점선
plt.plot(x, y1, 'r--', x, y2, 'g^-', x, y3, 'b*:', )

plt.axis([-30, 30, -30, 30])	# 그래프 범위 지정

plt.show()		# 맷플롯립 그래프 출력

