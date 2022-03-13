import cv2
global img1, img2

# 트랙바 변경 시 호출되는 함수 정의
def on_change_weight(x) :
    weight = x / 100	# 0~100 범위를 0.0~1.0 범위로 보정
    img_merged = cv2.addWeighted(img1, 1-weight, img2, weight, 0)	# 이미지 합성(weight 값에 따라)  
    cv2.imshow('Display', img_merged)	# 윈도우 창에 이미지 출력

# 윈도우 창(GUI) 출력
cv2.namedWindow('Display')

# 윈도우 창에 트랙바 추가(조절할 값의 이름, 창 이름, 최소값, 최대값, 트랙바 변경 시 호출할 함수)
cv2.createTrackbar('weight', 'Display', 0, 100, on_change_weight)

# 이미지 파일 읽기
img1 = cv2.imread('data/green_back.png')
img2 = cv2.imread('data/iceberg.png')

# 이미지 크기 변경
img1 = cv2.resize(img1, (300, 400))
img2 = cv2.resize(img2, (300, 400))
