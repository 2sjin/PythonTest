myInfo = "20194146/이승진/\n"
myInfo = myInfo.split('/')
print(myInfo[0] + " " + myInfo[1] + "\n")

s = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '
new_s = ""

print("[원시 데이터]")
print(s)
print(new_s)

s = s.lower()

for ch in s.split(' ') :	# 문자열을 띄어쓰기 단위로 분할
    if  ch == "kt" or ch == "skt" or ch == "samsung" or ch == "lg" : 
        new_s += "* "	  # 회사명은 ‘*’ 기호 1개로 변환하여 저장 
    else :
        new_s += ch + " "	  # 나머지 단어는 그대로 저장

print("[처리된 결과]")
print(new_s)
