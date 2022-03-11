# overalp 함수 정의(a, b는 매개변수)
# 초기 n 값은 a, b 중 길이가 짧은 문자열의 길이
def overlap(a, b) :
    if len(a) > len(b) : 
        n = len(a)
    else :
        n = len(b)

    # while문 : a의 뒤 n글자와 b의 앞 n글자가 같은지 if로 확인(초기 n부터 1까지 반복)
    while n > 0 : 
        if a[len(a)-n:] == b[:n] : 
            newStr = a[:len(a)-n] + b[:n] + b[n:] # 겹친 문자열 생성 후
            break                              # while문 탈출
        n -= 1

    # 1글자도 겹치지 않으면 a + b 문자열 생성
    if n <= 0 : 
        newStr = a + b 
    
    # 생성한 문자열 반환
    return newStr

# 두 문자열 입력 후 overlap 함수 실행 및 결과 출력
while True: 
    n1 = input("문자열1을 입력하시오 : ")
    n2 = input("문자열2을 입력하시오 : ")
    if n1 == n2 == '' :
        break    # 두 문자열이 모두 공백이면 종료
    else : 
        print(overlap(n1, n2))
