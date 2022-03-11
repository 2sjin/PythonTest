import csv
import matplotlib.pyplot as plt

f = open('source/weather.csv')	# csv 파일을 열어서 f에 저장
data = csv.reader(f)		# csv 파일 읽기	
header = next(data)		# 헤더 제거

monthly_wind = [ 0 for x in range(12) ]
days_counted = [ 0 for x in range(12) ]

for row in data :
    month = int(row[0][5:7])		# 0번 열에서 달 정보 추출
    if row[3] != '' :		# 풍속 데이터가 존재하는지 확인
        wind = float(row[3])		# 풍속 데이터 저장
        monthly_wind[month-1] += wind	# 해당 달에 풍속 데이터 추가
        days_counted[month-1] += 1		# 해당 달의 일수를 증가

for i in range(12) :
    monthly_wind[i] /= days_counted[i]	# 월별 평균 풍속 구하기

plt.bar(range(12), monthly_wind)		# 막대 그래프 생성
plt.xticks(range(12), range(1, 13))		# X축 눈금 설정(눈금 인덱스, 눈금 표시 값)
plt.title("20194146 Lee, Seung Jin")	# 차트 제목
plt.show()		# 맷플롯립 차트 출력

f.close()		# 파일 닫기
