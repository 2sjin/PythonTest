# 딕셔너리 이용하여 학번, 이름 출력
myName_dic = { 20194146: "이승진" }
for myID in myName_dic.keys() : 
    print(myID, myName_dic[myID], "\n")

# 딕셔너리 초기화
items = { " 커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5 }

while True :
    command = int(input("메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료 : "))
    if command == 1 : 
        name = input("[재고조회] 물건의 이름을 입력하시오: ")
        print('재고 :', items[name])	# 입력한 key에 해당하는 value 출력 
    if command == 2 :
        name, count = input("[입고] 물건의 이름과 수량을 입력하시오: ").split()
        items[name] += int(count)	# 입력한 key에 해당하는 value에 대한 가산 수행
    if command == 3 :
        name, count = input("[출고] 물건의 이름과 수량을 입력하시오: ").split()
        if int(count) > int(items[name]) :	# 입력한 count가 value(재고)보다 큰지 확인
            print("재고가 부족합니다.")
        else : 
            items[name] -= int(count)	# 입력한 key에 해당하는 value에 대한 감산 수행
    if command == 4 :
        print("프로그램을 종료합니다.")
        break;
