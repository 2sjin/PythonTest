import numpy as np

# 학번, 이름 표기(넘파이 배열)
infoArr = np.array(["20194146", "이승진"])
print(infoArr[0], infoArr[1], "\n")

# 정수 범위의 난수 생성 (x2~x4)
x1 = [ i for i in range(100) ]
x2 = [ i + np.random.randint(1, 10) for i in range(100) ]
x3 = [ i + np.random.randint(1, 50) for i in range(100) ]
x4 = [ np.random.randint(1, 100) for i in range(100) ]

print("x1 : \n", x1, "\n")
print("x2 : \n", x2, "\n")
print("x3 : \n", x3, "\n")
print("x4 : \n", x4, "\n")

# 피어슨(Pearson) 상관 계수 반환
result = np.corrcoef( [x1, x2, x3, x4] )

print(result)
