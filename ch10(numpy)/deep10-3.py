import numpy as np

# 학번, 이름 표기(넘파이 배열)
infoArr = np.array(["20194146", "이승진"])
print(infoArr[0], infoArr[1], "\n")

print("1)")
np.random.seed(100)		# 난수의 시드(seed) 설정
a = np.random.rand(3, 3, 3)		# 난수 생성(0.0~1.0), 배열의 크기는 3x3x3
print(a)

print()
a_max = np.max(a)	# 넘파이 배열 a의 최댓값 원소 출력
print("2) a의 원소들 중 최댓값 :", a_max)

print()
a_argmax = np.argmax(a)	# 넘파이 배열 a의 최대값 원소의 인덱스 출력
print("3) a의 원소들 중 최댓값의 위치 :", a_argmax)
