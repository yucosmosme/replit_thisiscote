#p.279
#서로소 집합을 활용한 사이클 판별 소스코드
#무방향 그래프에서 사이클이 생기는지 확인 가능
#모든 간선을 하나씩 확인하며 매 간선에 대하여 union, find 함수를 호출하는 방식

#루트노드 확인 함수
#부모노드에 저장된 노드가 루트노드일 때까지 재귀함수 호출
def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

#union 함수
def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a > b:
		parent[a] = b
	else:
		parent[b] = a

#노드개수, 간선개수 입력받기
v, e = map(int, input().split())

#노드개수만큼 부모테이블 만들기
#인덱스로 바로 접근 가능하도록 +1
parent = [0] * (v+1)

#부모테이블 노드번호로 초기화
for i in range(1, v+1):
	parent[i] = i
print('parent', parent)


#사이클 발생 여부 
cycle = False

#간선 정보 입력받아서
#사이클이 없다면 계속 union & find 진행하면서 루트노드 합친다
#이 과정에서 사이클이 생기면 루프를 멈춤
for _ in range(e):
	a, b = map(int, input().split())

	#a,b가 연결된 상태에서 둘의 루트노드가 같다는건 사이클이 존재한다는 뜻!!!
	if find_parent(parent, a) == find_parent(parent, b):
		cycle = True		
		break
	else:
		union_parent(parent, a, b)

print('parent', parent)
if cycle:
	print('사이클 발생')
else :
	print('사이클 없음')