#p.187 순차탐색
#이름 리스트 받음, 그 리스트에서 동빈 찾기
#걍포문 돌려서 함. 쉬움

names = list(map(str, input().split()))

search = input()

def searching():
	for i in range(len(names)):
		if (names[i] == search):
			print(i, names)
			return i


print('결과',searching())