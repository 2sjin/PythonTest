from fibo import *		# 함수가 있는 fibo.py 파일 불러오기

while True :
    i = int(input("몇 번째 항: "))
    showFib, showCount = fibonacci(i)	# 피보나치 함수 호출
    print(showFib)
    print("count=", showCount)
