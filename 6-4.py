#p.168 quick 정렬 - 널리 사용되는 직관적인 방법

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
	if start >= end: #원소가 1개인 경우 종료
		return 
	pivot = start #피벗은 첫번째 원소
	left = start + 1
	right = end

	#서로 엇갈리지 않는한 반복
	while left <= right:
		
		#피벗보다 큰 데이터를 찾을 때까지 반복
		while left <= end and array[left] < array[pivot]:
			left += 1
		#피벗보다 작은 데이터를 찾을 때까지 반복(작으면 값 셋팅)
		while right > start and array[right] >= array[pivot]:
			right -= 1

		#피벗 교체
		#엇갈렸다면 작은데이터와 피벗 교체
		if left > right:
			array[pivot], array[right] = array[right], array[pivot]
		#안엇갈렷다면 left right 교체
		else :
			array[left], array[right] = array[right], array[left]

	#분할한 뒤 오른쪽 왼쪽 각자 정렬 수행
	quick_sort(array, start, right-1)
	quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)