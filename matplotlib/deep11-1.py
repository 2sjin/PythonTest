import matplotlib.pyplot as plt

month = [7, 8, 9, 10, 11, 12]
users = [456, 492, 578, 599, 670, 854]

# 서브플롯을 추가하기 위한 도식 생성
fig = plt.figure()

# 서브플롯 추가(전체 행, 전체 열, 인덱스)
ax1 = fig.add_subplot(1, 4, 1)
ax2 = fig.add_subplot(1, 4, 2)
ax3 = fig.add_subplot(1, 4, 3)
ax4 = fig.add_subplot(1, 4, 4)

# 서브플롯에 그래프 추가
ax1.bar(month, users)			# 막대 그래프
ax2.plot(month, users)			# 직선 그래프
ax3.scatter(month, users, marker = '^')	# 산포도 그래프(삼각형 표식)
ax4.barh(month, users)			# 수평 막대 그래프

plt.title("Graph, 20194146, Lee, Seung Jin")  # 차트 제목

plt.show()	  # 맷플롯립 차트 출력
