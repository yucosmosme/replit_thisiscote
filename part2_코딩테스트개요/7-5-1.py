#p.197
#부품찾기
#이진탐색으로 구현

N = int(input('가게에 있는 부품개수'))
existList = list(map(int, input(str(N)+'개의 부품번호를 공백 기준으로 입력하시오.').split()))
print('N, existlist:', N, existList)

M = int(input('손님이 요청한 부품개수'))
askList = list(map(int, input(str(M)+'개의 부품번호를 공백 기준으로 입력하시오.').split()))
print('M, asklist:', M, askList)

#이진탐색으로 구현
#start, end, mid는 인덱스임
def searching(array, target, start, end):

	if start > end:
		return None
	mid = (start + end)//2

	if(target < mid):
		return searching(array, target, start, mid-1)
	elif(target > mid):
		return searching(array, target, mid+1, end)
	else:
		return mid


#요청부품 루프 돌면서 탐색함수 호출
for i in askList:
  result = searching(existList, i, 0, len(askList)-1)
  if result != None:
    print("yes", end=' ')
  else :
    print("no", end=' ')

#print('result:',result)
		