# ricecake
# p.201

#떡의 개수 N, 요청 떡의 길이 M
N, M = map(int, input().split())
#떡의 개별 높이 리스트
heightList = list(map(int, input().split()))

#떡을 높이 순으로 정렬
heightList.sort(reverse = True)

print('N,M,heightList: ', N,M,heightList)

#자르고 남은 떡 길이 리스트
leftList = []

#겉에 루프는 절단기 길이 리스트
for i in range(heightList[0], 0, -1):
	#떡길이 - i는 절단기 높이 = 남은떡길이
	#떡길이 계속 더해줌

	leftLength = 0
	print('i',i)
	#안에 루프는 떡 리스트
	for j in range(len(heightList)):
		print('i, j:',i, j)
		#떡별로 자르고 남은 길이 저장함
		if (i < heightList[j]) :
			leftLength += (heightList[j] - i)

	leftList.append(leftLength)

print(leftList)

#이진탐색으로 최대치의 떡길이를 찾는다.
#떡길이 리스트와 절단기 길이 리스트의 인덱스는 같으므로 그걸로 찾는다.
def searching(array, target, start, end):

	if start > end:
		('start > end', start)
		return start
		
	mid = (start + end)//2
	
	print('start, end', start, end)
	if (target < array[mid]):
		return searching(array, target, start, mid-1)
	elif(target > array[mid]):
		return searching(array, target, mid+1, end)
	else:
		print('mid',mid)
		return mid

print('leftList:', leftList)
res = searching(leftList, M, 0, len(leftList)-1)

print(heightList[0] - res)
	
