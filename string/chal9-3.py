import random
import string

myInfo = "20194146/이승진/\n"
myInfo = myInfo.split('/')
print(myInfo[0] + " " + myInfo[1] + "\n")

src_str = string.ascii_letters + "0123456789"	# 아스키 영문자(대/소문자) + 숫자 저장
print("src_str =", src_str, "\n")

size = int(input("몇 자리의 비밀번호를 원하십니까? "))
otp = ''

for i in range(size) : 
    randNum = random.randrange(0, 62)	# 0~61 범위의 난수 저장
    otp += src_str[randNum]	# 랜덤한 문자를 문자열 뒤에 결합
    
print(otp)

