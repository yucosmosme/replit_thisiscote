# ricecake
# p.201
# 이진탐색

#떡의 개수 N, 요청 떡의 길이 M
N, M = map(int, input().split())
#떡의 개별 높이 리스트
heightList = list(map(int, input().split()))

print('N,M,heightList: ', N,M,heightList)

#절단기 가능한 길이의 범위
#이진탐색 시작점과 끝점 
start = 0
end = max(heightList) #제일 긴 떡길이

#이진탐색 수행(반복적)
#절단기 길이 결과
result = 0
while(start<=end):
	#떡 길이 합
	total = 0
	#이진탐색 중간값
	mid = (start + end)//2
	#떡 개수만큼 루프 돌림
	for x in heightList:
		#잘랐을 때 떡의 양 계산
		#떡이 절단기보다 클 때만 자른다.
		if x > mid:
			total += x - mid

	#자른 결과 떡 길이의 합이 요청길이보다 작은경우
	#떡의 양이 부족한 경우 더 많이 자르기(왼쪽부분 탐색)
	if total < M:
		end = mid -1

	#떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
	else:
		result = mid #최대한 덜 잘랐을 때가 정답
		start = mid +1


#정답 출력
print(result)