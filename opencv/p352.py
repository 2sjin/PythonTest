import numpy as np
import cv2

org = cv2.imread('data/mandrill.png', 1)	# 이미지 파일 읽기

# 이미지 GaussianBlur 필터링하기
averaged55 = cv2.GaussianBlur(org, (5,5), 1)
averaged77 = cv2.GaussianBlur(org, (7,7), 1)

# 이미지 출력
cv2.imshow('original', org)
cv2.imshow('Gaussian 55', averaged55)
cv2.imshow('Gaussian 77', averaged77)
