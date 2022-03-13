# 딕셔너리 이용하여 학번, 이름 출력
myName_dic = { 20194146: "이승진" }
for myID in myName_dic.keys() : 
    print(myID, myName_dic[myID], "\n")


print("사전 프로그램 시작... 종료는 q를 입력")

# 빈 딕셔너리 초기화
dic = {}

while True :
    st = input('$ ')
    command = st[0]
    if command == '<' :	# 첫 글자 ‘<’ 입력 시
        st = st[1:]
        inputStr = st.split(':')	# [영어, 한글] 리스트 저장
        if len(inputStr) < 2 :	# 단어를 입력하지 않을 경우
            print("입력 오류가 발생했습니다.")
        else :
            dic[inputStr[0].strip()] = inputStr[1].strip()	# (key는 영어, value는 한글), strip()은 공백 제거
    elif command == '>' :	# 첫 글자 ‘>’ 입력 시
        st = st[1:]
        inputStr = st.strip()	# 공백 제거
        if inputStr in dic :	# 입력한 key(영어)에 해당하는 value(한글) 출력
            print(dic[inputStr])
        else :
            print("{}가 사전에 없습니다.".format(inputStr))
    elif command == 'p' :	# ‘p‘ 입력 시 딕셔너리 전체 출력
        print(dic)
    elif command == 'q' :	# ‘q‘ 입력 시 종료
        break
    else :
        print("입력 오류가 발생했습니다.")
print("사전 프로그램을 종료합니다.")
