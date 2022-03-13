# 딕셔너리 이용하여 학번, 이름 출력
myName_dic = { 20194146: "이승진" }
for myID in myName_dic.keys() : 
    print(myID, myName_dic[myID], "\n")

# 튜플을 요소로 갖는 2차원 리스트 초기화
student_tuple = [('211101', '강이안', '010-123-1111'),
                 ('211102', '박동민', '010-123-2222'),
                 ('211103', '김수정', '010-123-3333')]

# 빈 딕셔너리 초기화
student_dic = {}

print("\n 1. student_tuple 리스트 출력")
print(" ", student_tuple)

print("\n 2. (학번, 이름)의 딕셔너리 출력")
for student in student_tuple :
    number, name, phone = student
    student_dic[number] = [name, phone]	# 튜플의 요소를 딕셔너리에 추가
    print("  ", number, ":", name)		# 딕셔너리의 (key, value) 쌍을 순서대로 출력

# 입력한 key(학번)에 대한 value(이름, 연락처) 출력
print("\n 3. 학번으로 조회 결과 출력")
inputNum = input("  학번을 입력하시오 : ")
print("   " + inputNum + " 학생은 " + student_dic[inputNum][0] + "이며, \
전화번호는 " + student_dic[inputNum][1] + "입니다.")

