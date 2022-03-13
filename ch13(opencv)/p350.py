import numpy as np
import cv2

org = cv2.imread('data/mandrill.png', 1)	# 이미지 파일 읽기

kernel1 = np.ones((5, 5), np.float32) / 25	# 주변 24개의 픽셀에 평균값 적용
kernel2 = np.ones((7, 7), np.float32) / 49	# 주변 48개의 픽셀에 평균값 적용

# 이미지에 filter2D 필터 씌우기
averaged55 = cv2.filter2D(org, -1, kernel1)
averaged77 = cv2.filter2D(org, -1, kernel2) 

# 이미지 출력
cv2.imshow('original', org)
cv2.imshow('filtered1', averaged55)
cv2.imshow('filtered2', averaged77)
