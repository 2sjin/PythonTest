import re	

myInfo = "20194146/이승진/\n"
myInfo = myInfo.split('/')
print(myInfo[0] + " " + myInfo[1] + "\n")

text = '''
101 COM PythonProgramming1
102 MAT LinearAlgebra
103 ENG ComputerEnglish
'''

# 문자열 text 중 대문자(A~Z)가 연속 3번 반복되는 부분을 모두 출력
s = re.findall("[A-Z]{3}", text)
print(s)
