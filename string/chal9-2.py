myInfo = "20194146/이승진/\n"
myInfo = myInfo.split('/')
print(myInfo[0] + " " + myInfo[1] + "\n")

t = "It's Not The Right Time To Conduct Exams. MY DEMAND IN BOLD AND CAPITAL. NO EXAMS IN COVID!!!"

# 문자열 t에서 느낌표(‘!’) 개수 카운트 
print("느낌표 개수 : ", t.count('!'))

countTotal = countUpper = 0

for ch in t :
    countTotal += 1
    if ch.isupper() :	# 대문자일 경우
        countUpper += 1	# 카운트 1 증가

print("총 문자 개수 : ", countTotal)
print("대문자 개수 : ", countUpper)
