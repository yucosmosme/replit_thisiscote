#p.197
#부품찾기
#집합자료형으로 구현

N = int(input('가게에 있는 부품개수'))
existList = list(map(int, input(str(N)+'개의 부품번호를 공백 기준으로 입력하시오.').split()))
print('N, existlist:', N, existList)

M = int(input('손님이 요청한 부품개수'))
askList = list(map(int, input(str(M)+'개의 부품번호를 공백 기준으로 입력하시오.').split()))
print('M, asklist:', M, askList)

#요청부품 루프 돌면서 탐색
for i in askList:
	if i in existList:
    print("yes", end=' ')
  else :
    print("no", end=' ')

		