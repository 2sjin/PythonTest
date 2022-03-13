import turtle
t = turtle.Turtle()
t.shape("turtle")	
t.speed(0)		# 터틀의 이동 속도(클수록 빠르지만, 예외적으로 0은 최고 속도)

# 터틀 그래픽으로 학번, 이름 출력하는 함수 정의
def writeName() :
    t.penup()
    t.goto(-400, 200)
    t.pendown()
    t.write("20194146 이승진", font = ('맑은 고딕', 16, 'bold'))

# 이차함수 값 리턴하는 함수 정의
def f(x) :
    return x**2 + 1

# 좌표축 그리기
t.goto(200, 0)
t.goto(-200, 0)
t.goto(0, 0)
t.goto(0, 200)
t.goto(0, 0)

t.penup()
t.goto(-150, int(0.01*f(-150)))		# 함수 호출, 초기 위치(x = –150)로 터틀 이동
t.pendown()
for x in range(-150, 150):	# x축 범위는 –150 ~ 150
    t.goto(x, int(0.01*f(x)))	# 이차함수 함수 호출, 반환값으로 이동하며 그래프 그리기
writeName()    # 학번 이름 출력하는 함수 호출
