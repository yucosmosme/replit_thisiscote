#그래프 이론
#p.275 개선된 서로소 집합 알고리즘 소스코드

#개선된 속한 집합 찾기
def find_parent(parent, x):
	#받아온 변수 x라는 노드가 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
	a = find_parent(parent, a) #a의 루트노드
	b = find_parent(parent, b) #b의 루트노드
	# 더 작은 루트로드로 연결
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

#노드의 개수v와 간선(union 연산)의 개수e 입력받기
v, e = map(int, input().split())
#부모 테이블 초기화 - 테이블에 노드 개수만큼 그 노드의 부모노드가 있음
#+1개수로 해서 인덱스로 바로 접근
parent = [0] * (v + 1) 

#부모 테이블 상에서 부모를 자기 자신으로 초기화
#노드 1부터 시작 1,2,3,4,5...
#parent = [0 1 2 3 4 ...]
for i in range(1, v+1):
	parent[i] = i

#union 연산을 각각 수행
for i in range(e):
	#간선으로 연결된 노드 받기
	a, b = map(int, input().split())
	#합치기: 루트노드가 더 큰 애의 부모테이블에 더 작은 루트 부모를 저장함
	union_parent(parent, a, b)

#각 원소가 속한 집합 출력
#최종 루트노드가 표시됨 1 1 1 1 5 5 
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
	print(find_parent(parent, i), end=' ')

print()

#부모 테이블 내용 출력 : 개선된 find_parent로 인해 위의 루트노드와 부모테이블에 저장된 루트노드가 같아짐
#이걸로 부모테이블에 접그하면 바로 루트노드를 알수있어서 더욱 빠르게 접근 가능
#parent = [1 1 1 1 5 5] 
print('부모테이블: ', end='')
for i in range(1, v+1):
	print(parent[i], end=' ')
