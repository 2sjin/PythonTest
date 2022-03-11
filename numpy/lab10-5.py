import numpy as np

# 학번, 이름 표기(넘파이 배열)
infoArr = np.array(["20194146", "이승진"])
print(infoArr[0], infoArr[1], "\n")

players = [[170, 76.4, 23],
           [183, 86.2, 24],
           [181, 78.5, 25],
           [176, 80.1, 26]]

# 넘파이 배열 생성
np_players = np.array(players)

# 2차원 배열의 슬라이싱 및 논리적인 인덱싱
print('몸무게가 80 이상인 선수 정보')
print(np_players[np_players[:, 1] >= 80.0])
print('키가 180 이상인 선수 정보')
print(np_players[np_players[:, 0] >= 180.0])
print('나이가 25 이상인 선수 정보')
print(np_players[np_players[:, 2] >= 25])
