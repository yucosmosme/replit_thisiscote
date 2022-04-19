#p.183
#두배열의 원소교체
import operator

#원소개수 n개
n, k = map(int,input('n,k입력하시오').split())
print(n,k)

A = list(map(int, input(str(n)+'개의 자연수 입력하시오').split()))
print(A)

B = list(map(int, input(str(n)+'개의 자연수 입력하시오').split()))
print(B)


for i in range(k):

	#내가 직접 정렬해서 첫번째꺼 서로 교환하는 방법
	A.sort() #오름차순정렬
	B.sort(reverse=True) #내림차순 정렬

	#B가 A보다 크면 바꾼다. 작으면 바꾸면 안됨. 만약 작다면 더이상 바꿀게 없는 거기때문에 반복문을 탈출한다. 최대 교환개수 K 보다 적게 바꿔도 상관없는거임
	if A[0] < B[0]:
		temp = A[0]
		A[0] = B[0]
		B[0] = temp
	else:
    break		
	print('==================')

	#아래는 파이썬 오퍼레이터 이용하는 방법
	#A의 최소값 구하기
	#min_index, min_value = min(enumerate(A), key=operator.itemgetter(1))

	#B의 최대값 구하기
	#max_index, max_value = max(enumerate(B), key=operator.itemgetter(1))
	
	#A[min_index] = max_value
	#B[max_index] = min_value

print(A)
print(B)

sum = 0
for i in A:
	sum += i
print(sum)

#print(sum(A)) #이렇게 해도 됨