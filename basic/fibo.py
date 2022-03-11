def fibonacci(n) :	# 피보나치 함수 정의
    count = 0
    if n <= 0: 
        return "잘못된 입력입니다.", count
    elif n == 1 : 
        return 0, count
    elif n == 2 :
        return 1, count
    else: 
        a = 0    # 1번째 항
        b = 1    # 2번째 항
        for i in range(n-2) :	    # 1~2번째 항을 제외하고 반복횟수는 n-2
            c = a + b	# 3번째 항, 4번째 항, ..., n번째 항
            a = b		# 1번째 항, 2번째 항, ..., n-2번째 항
            b = c		# 2번째 항, 3번째 항, ..., n-1번째 항
            count += 1	# 함수(재귀함수 포함)가 호출 될 때마다 카운터 1씩 증가
        return c, count
