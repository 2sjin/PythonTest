import string

myInfo = "20194146/이승진/\n"
myInfo = myInfo.split('/')
print(myInfo[0] + " " + myInfo[1] + "\n")

src = input("문장을 입력하시오: ")
move = int(input("이동시킬 칸 수를 입력하시오 : "))

src_str = string.ascii_letters	# 모든 아스키 대/소문자를 나열한 문자열 저장("abcd...xyzABCD...XYZ")
dst_str = src_str[move:] + src_str[:move]	# 입력한 칸 수 만큼 src_str 이동(시프트)

# 매개변수를 암호화한 문자를 반환하는 함수 정의
def cipher(a) :
    idx = src_str.index(a)	# 매개변수가 src_str에서 몇 번째 인덱스에 있는지 idx에 저장
    return dst_str[idx]	# dst_str(시프트된 src_str)에서, 인덱스 idx에 있는 문자 리턴

for ch in src:	# 문자 하나씩 비교
    if ch in src_str:		# 알파벳일 경우
        print(cipher(ch), end="")	# 함수 호출 후 반환값 출력
    else :		# 알파벳이 아닐 경우
        print(ch, end="")	# 문자 그대로 출력
