#크루스칼 알고리즘

#신장트리: 하나의 그래프에서 모든 노드를 포함하지만 사이클이 존재하지 않는 부분 그래프
#최소 신장트리 알고리즘: 최소비용의 신장트리를 찾는 알고리즘 --> 대표적인게 크루스칼 알고리즘

#크루스칼 알고리즘은 그리디 알고리즘으로 분류됨.
#모든 간선을 오름차순으로 정렬 
#작은 애들부터 루프를 돌면서 find연산으로 루트노드가 안겹치는 (사이클이 없는) 아이들만 union연산 수행하여 신장트리에 추가함
#최종 신장트리에 포함된 간선의 비용의 합을 구한다.

#루트노드 확인 함수
#부모노드에 저장된 노드가 루트노드일 때까지 재귀함수 호출
def find_parent(parent, x):
	#루트 노드가 자기자신이 아니면 찾아냄
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])	
	return parent[x]

#두 원소의 집합 합치기
def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a > b:
		parent[a] = b
	else : 
		parent[b] = a
	
#노드개수, 간선개수 입력받기
v, e = map(int, input().split())

#노드개수만큼 부모테이블 초기화
#인덱스로 바로 접근 가능하도록 +1
parent = [0] * (v+1)

#부모테이블을 노드번호(자기자신)로 초기화
for i in range (1, v+1):
	parent[i] = i

#모든 간선을 담을 리스트
edges = []
#최종 비용을 담을 변수
result = 0

#간선 정보 입력받기
for i in range(e):
	#간선정보 연결노드 a, b와 그 비용 c
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

#간선을 비용순으로 정렬 - default는 튜플에서 첫번째 원소 기준으로 정렬함
edges.sort()

#간선을 하나씩 확인하며 union 실행. 
#단 루트노드가 같으면(사이클이 있으면) 패쓰
for edge in edges:
	#이렇게 먼저 선언해놓으면 안헷갈린다!!!
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost

print('parent: ', parent)
print('edges: ', edges)
print('total cost: ', result)
	
