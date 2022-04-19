#p.165 quick 정렬

array = [7,5,9,0,3,1,6,2,4,8]

pivot = array[0]

bigIdx = 0 #피벗보다 큰값
smallIdx = 0 #피벗보다 작은값



for i in range(1, len(array)): #1~9
	print('i',i, 'j',len(array)-i)
	if array[0] < array[i]:
		bigIdx = i
	else :
		break
	if array[0] > array[len(array)-i]:
		smallIdx = len(array)-i
	else 
	print('bigidx', bigIdx)
	print('smallIdx', smallIdx)
	
	#서로엇갈려있으면 
	if bigIdx > smallIdx:
		array[0], array[bigIdx] = array[bigIdx], array[0]
		break
		
	#값 교환
	elif smallIdx != 0 and bigIdx !=0:
		
		array[smallIdx], array[bigIdx] = array[bigIdx], array[smallIdx]
		#break
	print(array)
	
	#0으로 초기화
	bigIdx = 0
	smallIdx = 0
	
	

print(array)
	
		
