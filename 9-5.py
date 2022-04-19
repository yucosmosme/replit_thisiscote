# p.262
# 전보
# 한 지점에서 다른 모든 지점으로의 최단경로
#-> 다익스트라
# 한지점에서 출발하는거만 필요하므로 1차원 행렬
# 하나하나 비교하면서 최단거리인 점 선택하는 그리디와 유사 -> 우선순위큐
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

#도시 개수 n과 통로 개수 m, 메시지를 보내는 도시 C 입력
n, m, start = map(int, input().split())

graph = [[] for i in range(n+1)]
print(graph) # [[],[],[],[]] 빈 리스트로 만드는 이유: 각 리스트가 한 개의 점임. 그 점에서 다른 점으로 이동하는 거리들이 튜플로 들어가는거
#1에서 2로 4만큼 걸림, 1에서 3으로 2만큼 걸리면
#-> graph = [[], [(2,4), (3,2)], [], []]
#이 한개의 점에 있는 리스트에 있는 애들을 큐에 넣어서 제일 짧은 애가 먼저 선택되는거....

#최단 거리 테이블을 모두 무한으로 초기화
#start = 1이고 distance = [0,9,7..]이면
# 각 인덱스가 해당 목적지, 값이 거리
# 1에서 1로 가는 거리 0
# 1에서 2로 가는 거리 9
# 1에서 3으로 가는 거리 7이라는 뜻
distance = [INF] * (n+1) 
# distance = [INF,INF,INF,INF...]
# distance = [INF, 0, 4, 2]

#거리 정보 입력
for _ in range(m):
	#'도시 x에서 y로 이어지는 통로와 메시지 전달 시간 z를 입력: '
	x, y, z = map(int, input().split())
	graph[x].append((y,z))

#시작점 1에서 짧은 거리 순서대로 이동
#우선순위 큐적용
def dijkstra(start):
	q = []
	#시작노드 삽입
	heapq.heappush(q, (0, start))
	distance[start] = 0

	#큐에 있는 애들 하나씩 꺼내서 기존보다 짧은 경로이면 경로에 추가. 인접애들은 큐에 넣음.
	while q:
		#제일 짧은 거리, 제일 짧은 애
		dist, now = heapq.heappop(q)
		if distance[now] < dist:
			continue

		#새로운 애의 인접경로들 -  기존 저장 경로보다 짧으면 큐에 모두 추가해버림 (어차피 우선순위 큐라서 pop 할때 젤 짧은애가 꺼내짐)
		#[(2,4), (3,2)]
		for i in graph[now]:
			#이제까지 걸린 거리랑 새로운 거리 합치기
			cost = dist + i[1]
			#기존에 저장된 거리보다 짧으면 큐에 추가
			if cost < distance[i[0]]:
				heapq.heappush(q, (cost, i[0]))
				#거리정보에 저장
				distance[i[0]] = cost

#알고리즘 수행
dijkstra(start)
				
	
#print('graph',graph)
#print('distance', distance)

#도달 가능한 노드의 개수
count = 0
#총 걸리는 시간
max_distance = 0

for i in distance:
	#시작노드 제외, 도달 못하는애 제외
	if i < INF and i != 0:
		count += 1
		max_distance = max(max_distance, i)

print('count: ', count)
print('max distance: ', max_distance)






		