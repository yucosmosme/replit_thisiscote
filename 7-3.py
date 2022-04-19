#p.189
#이진탐색: 조건: 정렬되어있어야 함
#반복문으로 구현

#리스트 받음
list = list(map(int, input().split()))
print(list)

#정렬
list.sort()
print(list)

#찾는값
search = int(input())

start = 0
end = len(list)-1
mid = None

while(end - start >= 1):

	mid = (start+end)//2
	print('start,mid,end', start,mid,end)

	#찾는 원소가 없음
	if ((end-start)==1 and ((search > list[mid])and (search<list[end]))):
		mid = None
		break
		
	elif(search < list[mid]):
		print('if search, list[mid]',search, list[mid])
		#왼쪽 반으로 쪼개서넘김
		#재귀함수라서 각각 반환을 다 시켜줘야 함
		end = mid-1
		#mid = ((mid-1)+start)//2
		
	elif (search > list[mid]):
		print('elif search, list[mid]',search, list[mid])
		#오른쪽 반으로 쪼개서 넘김
		start = mid+1
		#mid = (end+(mid+1))//2
	
	else:
		print('else search, list[mid]',search, list[mid])
		break

		
#함수 실행
result = mid

if result == None:
	print("원소가 존재하지 않습니다.")
else :
	print(result+1) #일반인은 1부터 시작하니까