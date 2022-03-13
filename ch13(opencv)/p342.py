import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('data/mandrill.png')	# 이미지 파일 읽기
print(img[0:2])	# 이미지의 일부를 넘파이 배열로 변환하여 출력(0.0~1.0)
image_plot = plt.imshow(img)	# 맷플롯립 차트에 이미지 삽입
plt.show()		# 이미지 출력
