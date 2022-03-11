import numpy as np

# 학번, 이름 표기(넘파이 배열)
infoArr = np.array(["20194146", "이승진"])
print(infoArr[0], infoArr[1], "\n")

# 정수 범위에 해당하는 넘파이 배열 생성(range() 함수와 유사함) / 배열의 형태 변경(4x4x2)
a = np.arange(0, 32).reshape(4, 4, 2)

b = a.flatten()	# 1차원 넘파이 배열로 변환 
print("a : \n", a)
print("b : \n", b)
print()

# 넘파이 배열의 인덱싱
print("10번째 원소 :", b[9])
print("10번째 원소 :", b[19])
