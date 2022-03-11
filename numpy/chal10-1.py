import numpy as np

# 학번, 이름 표기(넘파이 배열)
infoArr = np.array(["20194146", "이승진"])
print(infoArr[0], infoArr[1], "\n")

# 넘파이 배열 생성
a = np.array(range(1, 11))    
b = np.array(range(10, 101, 10))

print("a=", a, "b=", b)

# 넘파이 배열 a, b의 각 요소별 산술 연산 수행
print("a+b=", a+b)
print("a-b=", a-b)
print("a*b=", a*b)
print("a/b=", a/b)
