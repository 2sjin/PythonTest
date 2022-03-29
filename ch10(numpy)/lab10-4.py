import numpy as np

# 학번, 이름 표기(넘파이 배열)
infoArr = np.array(["20194146", "이승진"])
print(infoArr[0], infoArr[1], "\n")

heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]
weights = [86, 74, 59, 95, 80, 68]

x = np.array([heights, weights])	# 넘파이 배열 생성
y = x[0:2, 1:3]	# 넘파이 배열의 슬라이싱
z = x[0:2][1:3]	# 리스트의 슬라이싱

print("x = ", x)
print("y = ", y)
print("z = ", z)
print("x shape :", x.shape)
print("y shape :", y.shape)
print("z shape :", z.shape)

bmi = x[1] / x[0]**2
print("BMI data")
print(bmi)
