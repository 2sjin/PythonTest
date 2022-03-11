
# 딕셔너리 이용하여 학번, 이름 출력
myName_dic = { 20194146: "이승진" }
for myID in myName_dic.keys() : 
    print(myID, myName_dic[myID], "\n")

# 2차원 튜플 초기화(학점 포)
student_tup = (('211101', '최성훈', '010-1234-4500', '4.3'),
               ('211102', '김은지', '010-2230-6540', '3.9'),
               ('211103', '이세은', '010-3232-7788', '4.25') )

# 빈 딕셔너리 초기화
student_dic = {}

# 튜플의 요소를 딕셔너리에 추가
for student in student_tup : 
    number, name, phone, grade = student
    student_dic[number] = [name, phone, grade]  # key는 학번, value는 [이름, 연락처, 학점]

# 딕셔너리의 (key, value) 쌍을 순서대로 출력
print("학생의 정보 목록")
for key, value in student_dic.items() : 
    print("{'" + key + "' : ", value, "}")

# 학점 평균 구하여 출력
avg = 0
for key_id in student_dic.keys() : 
    avg += float(student_dic[key_id][2])	# 각 리스트(value)의 2번째 요소
avg /= 3
print("전체 학생의 학점 평균 : %.2f" % avg)

# key(입력한 학번)에 해당하는 value(이름, 연락처) 출력
key_id = input("\n학번을 입력하시오 : ")
print("이름 : ", student_dic[key_id][0])
print("연락처 : ", student_dic[key_id][1])
