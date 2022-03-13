import re

myInfo = "20194146/이승진/\n"
myInfo = myInfo.split('/')
print(myInfo[0] + " " + myInfo[1] + "\n")

txt = "abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다."


# \S+	앞 부분에 공백이 아닌 문자가 연속 1개 이상 반복
# @	바로 뒤에 @가 1개
# [a-z.]+	바로 뒤에 알파벳 소문자 또는 마침표(‘.’)가 연속 1개 이상 반복
# 위 3가지 경우를 모두 만족하는 부분을 추출
output = re.findall("\S+@[a-z.]+", txt)


for i in output :
    i = i.split('@')
    print("추출된 아이디 : " + i[0] + " , 도메인 : " + i[1])
