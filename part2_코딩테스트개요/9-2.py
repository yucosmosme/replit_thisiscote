#p.249
#개선된 다익스트라 알고리즘
#우선순위 힙을 사용해서 연결 노드 중 최단거리인 아이를 맨 앞에 배치함 --> 내가 그다음 선택노드를 고르는 코드를 안만들어도 된다.

import heapq #우선순위 큐. 기본이 최소값 순으로 정렬
#(거리, 노드번호) 여기서 거리가 짧은 애 순서로 리스트가 정렬된다.
import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

#노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
#시작 노드 번호를 입력받기
start = int(input())

#노드정보(각 노드별로 연결노드와 그 거리가 저장되어있다. 개수는 n+1로 함으로써 [0]을 무시해서 index==노드번호가 되기때문에 노드에 쉽게 접근 가능)
#사용자 입력값에 의해 채워지는 값
graph = [[] for i in range(n+1)]
print('graph:', graph)
#graph = [[],[],[],[],[]......]빈 배열로 초기화됨

#최단 거리 테이블을 모두 무한으로 초기화
#얘가 내가 구할 값
distance = [INF] * (n+1) #[INF,INF,INF,INF...]

#모든 간선 정보를 입력받기
for _ in range(m):
	a, b, c = map(int, input().split())
	#a번 노드에서 b번노드로 가는 비용이 c
	graph[a].append((b,c))	

print('graph:', graph)
#ex. graph: [[],[(2,2), (3,5), (4,1)], .....,[]] 1번노드에 연결된 노드 2의 거리 2, 연결노드 3의 거리 5, 연결노드 4의 거리 1....

def dijkstra(start):
	#우선순위 큐 -- 방문노드에 연결된 노드들의 최소 거리 갱신하는애들을 여기에 넣어놓는다.
	#우선순위 큐이므로 항상 거리가 최소인 순으로 정렬된다.
	#큐에는 튜플형태로 들어가고, 튜플의 첫번째 원소를 기준으로 우선순위 큐를 구성하므로 (거리, 노드번호) 에 해당하는 튜플을 넣으면 된다.
	q = []
	
	#시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입 (시작노드가 1이면 1에서 1로 가는 거리는 0이니까 )
	#heappush(큐리스트, (연결노드에 가는 최소거리, 연결된노드))
	heapq.heappush(q, (0, start))
	distance[start] = 0

	#큐가 비어있지 않다면 
	#연결노드중에서 최단거리인 애들 꺼내서 최단거리 변수distance[]에 저장하고 --> 그 노드의 연결노드들을 최단거리 갱신할 애들있으면 우선순위큐에 넣는다. 
	while q:
		#맨 앞에있는애(거리 가장 짧은애) 꺼내서 변수저장
		dist, now = heapq.heappop(q)
		#우선순위큐에는 최단거리 갱신할떄마다 추가되므로 같은 노드가 중복 들어가있을수 있으므로 이미 방문한 애라면 무시해야함 (지금 큐에서 맨앞에 있는 노드의 거리보다 distance에 저장되어있느애가 더 짧다면 이미 처리된거)
		#한번 처리된건 처리되지 않기 때문에 개선된 알고리즘임!!!
		if distance[now] < dist:
			continue
		#현재 노드와 연결된 다른 인접노드들 확인
		for i in graph[now]:
			#i =(인접노드번호, 인접노드로가는거리)
			cost = dist + i[1] #거리 갱신
			#기존거리보다 짧으면 큐에 추가
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

#다익스트라 알고리즘 수행
dijkstra(start)

#이제 거리 출력
for i in distance:
	if i==INF:
		print("INFINITY", end=" ")
	else :
		print(i, end=" ")
		
		
		
		
	

