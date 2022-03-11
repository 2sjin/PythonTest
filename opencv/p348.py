import numpy as np
import cv2

# 이미지 파일 읽기
image = cv2.imread('data/mandrill.png')		# BGR 모드(기본)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)	# HSV 모드

red_low = np.array([0, 0, 0])		# 추출할 색상의 아래쪽 경계(색상, 채도, 명도)
red_high = np.array([25, 255, 255])	# 추출할 색상의 위쪽 경계(색상, 채도, 명도)

my_mask = cv2.inRange(image_hsv, red_low, red_high)	# 이미지에서 색상 경계 범위에 해당하는 픽셀 찾기
extracted = cv2.bitwise_and(image, image, mask=my_mask)	# 이미지의 AND 마스크 결과

# 이미지 출력
cv2.imshow('original', image)
cv2.imshow('mask', my_mask)
cv2.imshow('extracted', extracted)

