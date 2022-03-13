import numpy as np
import cv2

# 이미지 파일 읽기 및 필터링
original_image = cv2.imread('data/salt_pepper.png', 0)		# 원본
result_image1 = cv2.GaussianBlur(original_image, (9,9), 1)		# 가우스 필터
result_image2 = cv2.bilateralFilter(original_image, 9, 50, 50)	# 양방향 필터
result_image3 = cv2.medianBlur(original_image, 9)		# 중앙값 필터

# 이미지 출력
cv2.imshow('orginal', original_image)
cv2.imshow('GaussianBlur', result_image1)
cv2.imshow('bilateralFilter', result_image2)
cv2.imshow('medianBlur', result_image3)
