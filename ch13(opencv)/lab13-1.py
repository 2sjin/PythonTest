import numpy as np
import cv2

# 이미지 파일 읽기
img1 = cv2.imread('data/green_back.png')
img2 = cv2.imread('data/iceberg.png')

# 이미지 크기 조절
front_image = cv2.resize(img1, (300, 400))
back_image = cv2.resize(img2, (300, 400))

img_hsv = cv2.cvtColor(front_image, cv2.COLOR_BGR2HSV)	# 이미지를 HSV 모드로 저장
l_bound = np.array([40, 100, 50])	# 녹색의 아래쪽 경계(색상, 채도, 명도)
u_bound = np.array([80, 255, 255])	# 녹색의 위쪽 경계(색상, 채도, 명도)

my_mask = cv2.inRange(img_hsv, l_bound, u_bound)	# 녹색의 경계를 바탕으로 녹색 픽셀 찾기
mask_inv = cv2.bitwise_not(my_mask)			# 녹색이 아닌 픽셀 찾기(NOT 마스크)

removed = cv2.bitwise_and(front_image, front_image, mask=mask_inv)	# 녹색이 아닌 픽셀만 출력
extracted = cv2.bitwise_and(front_image, front_image, mask=my_mask)	# 녹색 픽셀만 출력
background = cv2.bitwise_and(back_image, back_image, mask=my_mask)	# 녹색 픽셀 영역에 배경 출력
merged = cv2.bitwise_or(removed, background)		# 녹색이 아닌 픽셀과 배경 합치기(OR 마스크)

# 이미지 출력
cv2.imshow('mask', my_mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('removed', removed)
cv2.imshow('extracted', extracted)
cv2.imshow('background', background)
cv2.imshow('merged', merged)
