#p.189
#이진탐색: 조건: 정렬되어있어야 함
#재귀함수로 구현

#리스트 받음
list = list(map(int, input().split()))
print(list)

#정렬
list.sort()
print(list)

#찾는값
search = int(input())

def searching(start, mid, end): #매개변수 인덱스받음
	print('start mid end', start,mid,end)

	if(mid==end or start == end):
		return None
		
	elif(search < list[mid]):
		print('if',search, list[mid])
		#왼쪽 반으로 쪼개서넘김
		#재귀함수라서 각각 반환을 다 시켜줘야 함
		return searching(start, ((mid-1)+start)//2, mid-1)
		
	elif (search > list[mid]):
		print('elif',search, list[mid])
		#오른쪽 반으로 쪼개서 넘김
		return searching(mid+1, (end+(mid+1))//2 ,end)
	
	else:
		print('else',search, list[mid], mid)
		return mid



#함수 실행
result = searching(0, (len(list)-1)//2, len(list)-1)

if result == None:
	print("원소가 존재하지 않습니다.")
else :
	print(result+1) #일반인은 1부터 시작하니까