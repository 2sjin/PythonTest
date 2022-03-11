# 딕셔너리 이용하여 학번, 이름 출력
myName_dic = { 20194146: "이승진" }
for myID in myName_dic.keys() : 
    print(myID, myName_dic[myID], "\n")

# 딕셔너리 초기화
fruits_price = {'사과':0, '배':0, '수박':0, '귤':0, '포도':0}

# 입력한 문자열 값들로 리스트 초기화
inputPriceList = input("사과, 배, 수박, 귤, 포도 가격을 공백으로 구분하여 입력: ").split()

print("------------ 오늘의 과일 가격 ------------")
i = 0

# 딕셔너리의 각 key(과일)에 해당하는 value(가격)를 차례대로 출력
for f in fruits_price.keys() :
    fruits_price[f] = inputPriceList[i]
    print(f + " :　 " + fruits_price[f] + "원")
    i += 1

# 입력한 key(과일)에 해당하는 value(가격) 출력
while True :
    fruit = input("구매를 원하는 과일의 이름을 입력하시오 : ")
    print("오늘의", fruit, "가격은", fruits_price[fruit], "원 입니다.")
