#p.259
#미래도시
#1번회사에서 k번회사 거쳐서 x번 회사 가는데 걸리는 최소 거리는?
#거쳐가는거,
#모든경로에서 모든경로 거리 저장할 2차원 행렬 필요
#플로이드 워셜 알고리즘

n, m = map(int, input('회사개수 n과 연결 간선 개수 m 입력: ').split())
INF = int(1e9)

k, x = map(int, input('소개팅할 회사 k와 목적 방문회사 x 공백 기준 입력:').split())

#인덱스 맞추려고 열,행개수 +1
#거리정보
graph = [[INF] * (n+1) for _ in range(n+1)]

#print(graph)

#자신한테 가는길은 0으로 셋팅
for i in range(1, n+1):
	for j in range(1, n+1):
		if i == j :
			graph[i][j] = 0

#print(graph)

#연결간선 거리 1로 셋팅
for i in range(m):
	a, b = map(int, input('연결간선 공백 기준 입력: ').split())
	graph[a][b] = 1
	graph[b][a] = 1

#print(graph)

#점화식에 따라 플로이드 워셜 알고리즘 수행
#a에서 출발해서 k를 거쳐서 b로 도착
for k in range(1, n+1):
	for a in range(1, n+1):
		for b in range(1, n+1):
			
			graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

print(graph)
			
#수행결과 출력
distance = graph[1][k] + graph[k][x]

print('distance: ',distance)

if distance >= INF:
	print(-1)
else :
	print(distance)