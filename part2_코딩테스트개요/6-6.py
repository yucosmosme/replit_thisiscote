#p.174 계수정렬

list = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

#리스트 생성시 크기 지정하고 0으로 초기화
#list에서 가장 큰값을 리스트의 크기로 지정한다.
#print(max(list))
result = [0 for i in range(max(list)+1)]

for i in range(len(list)):
	#print(list[i])
	#각데이터에 해당하는 인덱스 값 증가
	result[list[i]] += 1

print(result)

newRes = []

# 리스트에 기록된 정렬정보 확인
for i in range(len(result)):
	for j in range(result[i]):
		#print(i)
		newRes.append(i)
		
print(newRes)
	
	
		

