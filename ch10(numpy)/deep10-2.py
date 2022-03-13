import numpy as np

# 학번, 이름 표기(넘파이 배열)
infoArr = np.array(["20194146", "이승진"])
print(infoArr[0], infoArr[1], "\n")

print("1)")
n_arr = np.arange(25).reshape(5,5)	# 정수 범위에 해당하는 넘파이 배열 생성 / 배열의 형태 변경(5x5)
print(n_arr)
print("")

print("2)")
print("첫 원소 :", n_arr[0, 0])		# 넘파이 배열의 슬라이싱
print("마지막 원소 :", n_arr[-1, -1])	# 넘파이 배열의 슬라이싱
print("")

print("3)")
print(n_arr[:2])	# 넘파이 배열의 슬라이싱
print("")

print("4)")
print(n_arr[2:])	# 넘파이 배열의 슬라이싱
print("")

print("5)")
print(n_arr[:, ::2])	# 넘파이 배열의 슬라이싱
print("")

print("6)")
print(n_arr[::2, ::2])	# 넘파이 배열의 슬라이싱
print("")

print("7)")
print(n_arr[:2].reshape(5,2))	# 넘파이 배열의 슬라이싱 / 배열의 형태 변경(5x2)
print("")
