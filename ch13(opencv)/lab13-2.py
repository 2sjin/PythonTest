import numpy as np
import cv2

# 이미지 파일 읽기 및 필터링
img = cv2.imread('data/book.png')
blur_bilateral = cv2.bilateralFilter(img, 11, 75, 75)		# 양방향 필터
gray_img = cv2.cvtColor(blur_bilateral, cv2.COLOR_BGR2GRAY)	# 양방향 필터 + 회색조

# 양방향 필터 + 회색조 이미지를 임계값(인근 픽셀과 비교하는 적응적 임계값)에 따라 이진화
thresh = cv2.adaptiveThreshold(gray_img, 255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 7)

# 이미지 출력
cv2.imshow('orginal', img)
cv2.imshow('bilateral', blur_bilateral)
cv2.imshow('gray', gray_img)
cv2.imshow('binary', thresh)
