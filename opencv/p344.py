import cv2	# OpenCV 불러오기

img = cv2.imread('data/mandrill.png', 1)	# 이미지 파일 읽기

cv2.rectangle(img, (20,200), (200,20), (0,0,0), 5)		# 사각형 그리기(이미지, 시작점, 끝점, 색상, 두께)
cv2.line(img, (20,20), (200,200), (0,0,255), 5)		# 직선 그리기(이미지, 시작점, 끝점, 색상, 두께)
cv2.arrowedLine(img, (20,200), (200,20), (0,0,255), 5)	# 화살표 그리기(이미지, 시작점, 끝점, 색상, 두께)

# 텍스트 삽입
cv2.putText(img, "Hello!!!", (40, 225), fontFace = 2, fontScale = 0.75, color = (0,0,0))

# 이미지 출력
cv2.imshow('lined', img)

