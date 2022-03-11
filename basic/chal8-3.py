# 딕셔너리 이용하여 학번, 이름 출력
myName_dic = { 20194146: "이승진" }
for myID in myName_dic.keys() : 
    print(myID, myName_dic[myID], "\n")

# 리스트의 값을 집합으로 변환(순서와 중복이 없음)
partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

# 교집합 출력
print("파티 A, B에 참석한 사람들 : ", end=" ")
for i in partyA | partyB :
    print(i, end=" ")
print("")

# 합집합 출력
print("파티 A, B에 중복없이 참석한 사람 : ", end=" ")
for i in partyA ^ partyB :
    print(i, end=" ")
print("")

# 차집합 출력
print("파티 A에만 참석한 사람 : ", end=" ")
for i in partyA - partyB :
    print(i, end=" ")

# 문자열로 이루어진 집합의 순서는 랜덤하게 출력됨
