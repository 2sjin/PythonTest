import turtle
t = turtle.Turtle()

t.speed(0)		# 터틀의 이동 속도(클수록 빠르지만, 예외로 0은 최고 속도)
t.width(2)		# 터틀이 그리는 선의 두께

angle = count = 0

# 무한 루프(break를 만나면 탈출)
while True:
    t.penup()
    t.goto(-350 + count * 250, 0)
    t.pendown()

    length = 4

    angle = int(input("각도를 입력하시오: "))

    if angle < 0 : 
        break	# 입력한 각도가 음수이면 반복문 탈출
    else : 
        while length < 200:
            t.forward(length)
            t.right(angle)
            length += 2  
        count += 1

print("*** 터틀 그래픽을 종료합니다 ***")
