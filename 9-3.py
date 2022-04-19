#p.257
#플로이드 워셜 알고리즘

INF = int(1e9) #무한을 의미하는 10억

#노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input()) #뱡향 서로 다른건 따로따로임

#2차원 리스트(그래프 표현)를 만들고 모든 값을 무한으로 초기화
#[INF]*(n+1)을 range()만큼 반복
#접근이 용이하게 인덱스번호랑 같게 해주는거라
#0번째는 다 무시하면 된다.
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
	for b in range(1, n+1):
		if a == b:
			graph[a][b] = 0
#print(graph)

#각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
	#a에서 b로 가는 비용 c
	a, b, c = map(int, input().split())
	graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘 수행
#a에서 출발해서 k를 거쳐서 b로 도착
for k in range(1, n+1):
	for a in range(1, n+1):
		for b in range(1, n+1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행된 결과를 출력
for a in range(1, n+1):
	for b in range(1, n+1):
		#도달할 수 없는 경우, 무한이라고 출력
		if graph[a][b] == INF:
			print("infinity", end=" ")
		else:
			print(graph[a][b], end=" ")
	print()


			