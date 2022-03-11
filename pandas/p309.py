print("20194146 이승진 \n")

import csv

f = open('data/weather.csv')	# csv 파일을 열어서 f에 저장
data = csv.reader(f)		# csv 파일 읽기	
header = next(data)		# 헤더 제거
i = 0
for row in data :
     print(row)	# 한 줄씩 반복적으로 데이터 출력
     i += 1
     if (i >= 10) :	
         break	# 10줄을 초과하면 반복 중단
f.close()	# 파일 닫기
