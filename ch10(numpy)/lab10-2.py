import numpy as np

# 학번, 이름 표기(넘파이 배열)
infoArr = np.array(["20194146", "이승진"])
print(infoArr[0], infoArr[1], "\n")

heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]
weights = [86, 74, 59, 95, 80, 68]

# 넘파이 배열 생성
np_heights = np.array(heights)
np_weights = np.array(weights)	

bmi = np_weights / (np_heights**2)
print('대상자들의 키:', np_heights)

# 넘파이 배열의 논리적인 인덱싱
print('키가 1.80 이상인 사람:', np_heights[np_heights >= 1.80])
print('대상자들의 몸무게:', np_weights)
print('몸무게가 85 이상인 사람:', np_heights[np_weights >= 85])
print('대상자들의 BMI:')
print(bmi)
print('BMI가 27 이상인 사람:', bmi[bmi >= 27])
