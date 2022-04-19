#p.178 정렬 실전문제
#위에서 아래로

#내림차순정렬
print('1<=N<=500 사이의 수의 개수를 입력하시오')
n = int(input())

list = []
for i in range(n):
	list.append(int(input('1이상 100,000이하의 자연수를 입력하시오')))
print(list)

#주어진 수열을 내림차순으로 정렬하여 공백으로 구분하여 출력. 
#파이썬 정렬 라이브러리 사용
list.sort(reverse=True)
print(list)
for i in list:
	print(i,end=" ")
	