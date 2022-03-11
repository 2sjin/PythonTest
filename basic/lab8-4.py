# 딕셔너리 이용하여 학번, 이름 출력
myName_dic = { 20194146: "이승진" }
for myID in myName_dic.keys() : 
    print(myID, myName_dic[myID], "\n")

# process 함수 정의(w는 매개 변수)
def process(w) :
    output =""
    for ch in w :		# 문자열의 문자 1개씩 체크
        if ch.isalpha() :	# 문자가 알파벳이면
            output += ch	# 임시 문자열에 추가
    return output.lower()	# 문자열을 소문자로 반환

words = set()	# 빈 집합 초기화
fname = input("입력 파일 이름: ")
file = open(fname, "r")	# 파일 열기
overlap = 0

for line in file :
    lineWords = line.split()
    for word in lineWords :
        word = process(word)    # process() 함수로 단어를 소문자로 변환
        if word in words :      # 단어가 words 집합에 이미 있다면
            overlap += 1        # 중복 개수 1 증가
        words.add(word)         # 중복된 단어를 집합에 추가하면 자동으로 제거됨 
        
print("사용된 단어의 개수 =", len(words))
print("중복된 단어의 개수 =", overlap)
print(words)
                                            
# 문자열로 이루어진 집합의 순서는 랜덤하게 출력됨
