import turtle

t = turtle.Turtle()
t.color("blue")	# 터틀 및 터틀이 그리는 선의 색상
t.pensize(3)	# 터틀이 그리는 선의 두께
t.hideturtle()  # 터틀 숨기기(t.showturtle() 하면 터틀 보이기)

# 터틀 그래픽으로 학번, 이름 출력하는 함수 정의
def writeName() : 
    t.penup()
    t.goto(-300, 400)
    t.pendown()
    t.write("20194146 이승진", font = ('맑은 고딕', 16, 'bold'))

# 그래프 그리기
def drawBar(height) :
    if height < 100 :	# 매개변수의 값이 100 미만이면
        t.fillcolor("blue")	# 터틀의 채우기 색상 설정(파랑)
    elif height < 300 :	# 300 미만이면
        t.fillcolor("yellow")	# 터틀의 채우기 색상 설정(노랑)
    else : 		# 300 이상이면
        t.fillcolor("red")	# 터틀의 채우기 색상 설정(빨강)

    t.begin_fill()	# 채우기 시작
    t.left(90)
    t.forward(height)
    t.write(str(height), font = ('Times New Roman', 16, 'bold'))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()	# 채우기 종료

data = [120, 56, 309, 220, 156, 23, 98]
for d in data:
    drawBar(d)	# 그래프 그리기 함수 호출(리스트 내 요소를 차례대로 대입)
writeName()    # 학번 이름 출력하는 함수 호출
