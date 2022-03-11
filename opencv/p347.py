import cv2

# 이미지 파일 읽기
mask_image = cv2.imread('data/mask_circle.png')
back_image = cv2.imread('data/iceberg.png')

# 이미지 크기 변경
mask_image = cv2.resize(mask_image, (300, 400))
back_image = cv2.resize(back_image, (300, 400))

# 이미지에 마스크 씌우기(AND, OR, XOR)
mask_ANDed = cv2.bitwise_and(mask_image, back_image)
mask_ORed = cv2.bitwise_or(mask_image, back_image)
mask_XORed = cv2.bitwise_xor(mask_image, back_image)

# 이미지 출력
cv2.imshow('mask', mask_image)
cv2.imshow('back', back_image)
cv2.imshow('mask and', mask_ANDed)
cv2.imshow('mask or', mask_ORed)
cv2.imshow('mask xor', mask_XORed)
