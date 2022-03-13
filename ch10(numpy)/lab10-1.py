import numpy as np

# 학번, 이름 표기(넘파이 배열)
infoArr = np.array(["20194146", "이승진"])
print(infoArr[0], infoArr[1], "\n")

# 실습 1 : 리스트 요소를 입력하여 넘파이 배열 생성
array_a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print('실습 1 : array_a =', array_a)

# 실습 2 : range() 사용하여 넘파이 배열 생성
array_b = np.array(range(10))
print('실습 2 : array_b =', array_b)

# 실습 3 : range() 사용하여 짝수 넘파이 배열 생성
array_c = np.array(range(0, 10, 2))
print('실습 3 : array_c =', array_c)

# 실습 4 : 넘파이 배열의 속성 출력
print('실습 4: ')
print('array_c의 shape :', array_c.shape)	# array_c의 크기 반환
print('array_c의 ndim :', array_c.ndim)		# array_c의 차원의 개수 반환
print('array_c의 dtype :', array_c.dtype)	# array_c의 원소의 자료형 반환
print('array_c의 size :', array_c.size)		# array_c의 원소의 개수 반환
print('array_c의 itemsize :', array_c.itemsize)	# array_c의 원소 1개 당 크기(bytes) 반환 
