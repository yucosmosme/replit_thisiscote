#p.197
#부품찾기
#순차탐색으로 구현

N = int(input('가게에 있는 부품개수'))
existList = list(map(int, input(str(N)+'개의 부품번호를 공백 기준으로 입력하시오.').split()))
print('N, existlist:', N, existList)

M = int(input('손님이 요청한 부품개수'))
askList = list(map(int, input(str(M)+'개의 부품번호를 공백 기준으로 입력하시오.').split()))
print('M, asklist:', M, askList)

#순차탐색으로 구현 (for루프돌려서 하나씩 비교)
def searching(targetN):
	ifExist = False
	for i in range(len(existList)):
		#print('n, targetN, ifExist::::',N, targetN, ifExist)
		if existList[i] == targetN:
			ifExist = True
	return ifExist

for i in range(M):
  result = searching(askList[i])
  #print(askList[i],'result:::', result)
  if True == result :
    print("yes", end=' ')
  else :
    print("no", end=' ')

#print('result:',result)
		