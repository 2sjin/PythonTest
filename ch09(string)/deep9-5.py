import re

myInfo = "20194146/이승진/\n"
myInfo = myInfo.split('/')
print(myInfo[0] + " " + myInfo[1] + "\n")

s = 'Korea is awesome! I REALLY LOVE KOREA.'
print("s =", s)
korea = re.findall('[Kk][Oo][Rr][Ee][Aa]', s)	# 대소문자 구분 없이 모든 Korea 부분을 추출
print("Korea의 출현 횟수 : ", len(korea))
