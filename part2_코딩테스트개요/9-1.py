#p.237
#Dijkstra 최단경로
#사실은 최단경로가 아니고 그냥 최단거리만 구하는 문제로 보통 출제된다.

#입력데이터가 많으면 input()보다 빠른 sys.std.realine()로 입력받는다.
import sys

input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값으로 10억을 설정(최단거리 초기화에 들어갈 값)

#노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
#시작 노드 번호를 입력받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
#노드번호==리스트의index가 되면 접근하기 쉬우니까 리스트 크기 0은 무시하고 1부터 데이터가 들어가도록 n+1로 셋팅
graph = [[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
#이게 내가 구할것
#start 지점에서 각 지점으로 가는 최단거리테이블
#경로는 안나옴
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
	a, b, c = map(int, input().split())
	#a번 노드에서 b번 노드로 가는 비용이 c라는 의미

	#graph에서 n번째노드에 연결된 노드와 그 비용 c를 모두 추가한다.
	graph[a].append((b, c))

print('graph:', graph)
#ex. graph: [[],[(2,2), (3,5), (4,1)], [....], []

#그 다음 방문노드 고르기
#방문하지 않은 노드 중에서 가장 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
	#먼저 최소값을 무한대로 셋팅한 다음 노드들을 루프 돌면서 방문 안했고, min_vaue보다 더 작은 거리값을 가진 노드가 있으면 그 노드번호 반환
	#-> 이게 그 다음 방문할 노드가 된다.
	min_value = INF
	for i in range(1, n+1):
		if distance[i] < min_value and not visited[i]:
			min_value = distance[i]
			index = i
	return index

def dijkstra(start):
	#시작 노드에 대해서 초기화
	#노드별 방문에 걸리는 거리
	distance[start] = 0 #[INF, 0, INF, INF, INF, INF, INF]
	#노드별 방문 여부
	visited[start] = True #[False, True, False, False, False, False, False]
	print('distance', distance)
	print('visited', visited)

	#시작노드에만 적용
	#시작노드에 해당하는 graph[1]에 저장된 연결노드와 그 비용[(2,2), (3,5), (4,1)]리스트 포문돌림 -> distance[]변수에 비용 저장.
	for j in graph[start]:
		distance[j[0]] = j[1] #distance[시작노드에 연결된 노드] = 그 노드에 가는 비용
	print('distance2', distance)
	# distance = [INF, 0, 2, 5, 1, INF, INF]
		
	#시작 노드를 제외한 전체 n-1개 노드에 대해 반복
	for i in range(n-1):

		#그다음 방문노드 고르기
		#현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
		now = get_smallest_node()
		visited[now] = True
		#현재 노드와 연결된 다른 노드를 확인
		#예를 들어 방문노드 now가 4이면
		#graph[4] = [(3,3), (5,1)] --> 4번노드에 연결된 3번노드까지 3거리 걸리고, 연결된 5번노드까지 1걸림
		#연결된 노드 포문돌려서
		for j in graph[now]:
			#이제까지 방문해온 거리 + 연결노드에 걸리는 거리 합계 구함
			cost = distance[now] + j[1]
			#위에꺼가 기존에 해당 연결노드에 저장된 거리보다 작을때애만 갱신하고 아니면 무시한다.
			if cost < distance[j[0]]:
				distance[j[0]] = cost

#다익스트라 알고리즘 수행
dijkstra(start)

#위에서 계산은 다 끝났고 이제 출력만 하면됨
#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
	#도달할 수 없는 경우 무한(INFINITY)라고 출력
	if distance[i] == INF:
		print("INFINITY")
	#도달할 수 있는 경우 거리를 출력
	else:
		print(distance[i], end=" ")
