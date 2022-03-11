import re

myInfo = "20194146/이승진/\n"
myInfo = myInfo.split('/')
print(myInfo[0] + " " + myInfo[1] + "\n")

s = "Jian777 is very famous Data scientist. He is only 26 years old but published 19 papers."

listEng = []
listNum = []
listEngNum = []

for ch in re.split(" |\.", s) :	# 문장을 공백 또는 마침표(‘.’)를 기준으로 추출 
    if ch in re.findall("[a-z|A-Z]+[0-9]+", s) :	# 영문자+숫자로 이루어진 모든 단어 추출
        listEngNum.append(ch)
    elif ch in re.findall("[a-z|A-Z]+", s) : 	# 모든 영단어 추출
        listEng.append(ch)
    elif ch in re.findall("[0-9]+", s) : 		# 모든 숫자 추출
        listNum.append(ch)

print("영문 단어 :", end=" ")
for ch in listEng :
    print(ch, end=" ")
print()

print("숫자 :", end=" ")
for ch in listNum :
    print(ch, end=" ")
print()

print("영문자+숫자 :", end=" ")
for ch in listEngNum :
    print(ch, end=" ")

