import random

q = []	# 빈 리스트 초기화

# 리스트에 수학문제 추가
q.append("1 + 2 = {}".format(1 + 2))
q.append("32 + 64 = {}".format(32 + 64))
q.append("1755 + 250 = {}".format(1755 + 250))
q.append("10 - 5 = {}".format(10 - 5))
q.append("209 - 75 = {}".format(209 - 75))
q.append("1000 - 456 = {}".format(1000 - 456))
q.append("70 * 6 = {}".format(70 * 6))
q.append("125 * 125 = {}".format(125 * 125))
q.append("300 / 50 = {}".format(300 / 50))
q.append("1024 / 64 = {}".format(1024 / 64))

print("#########################")
print("#    오늘의 수학문제    #")
print("#########################")
print("")

count = 0

while True :
    count += 1
    Question = random.choice(q)	# 리스트 q의 요소 1개를 무작위로 반환
    print("문제", count, ".", Question)
    n = 0
    while n != -1 and n != 1 :      # -1, 1 이외의 값 입력 시 input 반복
        n = int(input("마치려면 -1, 계속하려면 1: "))
    if n == -1 :       		# 입력이 -1이면 종료, 아니면 while 반복
        break

