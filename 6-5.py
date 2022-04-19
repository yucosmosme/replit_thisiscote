#p.169 quick 정렬 - 파이썬의 장점을 살린 방법

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
	#리스트가 하나 이하의 원소만을 담고 있다면 종료
	if len(array) <= 1:
		return array

	pivot = array[0] #피벗은 첫번째 원소
	tail = array[1:] #피벗을 제외한 리스트



	#리스트 내포 문법 (list comprehension)
	#[출력값 for 항목 in 반복가능객체 if 조건문]

	#[x출력 tail리스트에서 for문돌려서 pivot보다 작은 애들만]
	left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
	right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

	#분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
	return quick_sort(left_side) + [pivot] + quick_sort(right_side)
	
print(quick_sort(array))

