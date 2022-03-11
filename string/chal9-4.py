import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

myInfo = "20194146/이승진/\n"
myInfo = myInfo.split('/')
print(myInfo[0] + " " + myInfo[1] + "\n")

wiki = wikipedia.page('Python')	# 위키피디아 컨텐츠 제목 명시
text = wiki.content			# 위키피디아의 ‘Python’ 페이지에서 텍스트 컨텐츠 추출

wordcloud = WordCloud(width = 2000, height = 1500).generate(text)	# 워드클라우드 이미지 생성

plt.figure(figsize=(40, 30))	# 맷플롯립 속성 변경(크기=(40, 30))
plt.imshow(wordcloud)	# 맷플롯립에 워드클라우드 이미지 포함
plt.show()			# 맷플롯립 출력
