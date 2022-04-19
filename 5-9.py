# p.147 BFS

from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
  #큐 라이브러리 deque 사용
  queue = deque([start]) #1이 들어간 큐 생성
  #현재 노드를 방문 처리
  visited[start] = True
  #큐가 빌때까지 반복
  while queue: #큐에 원소가 있을때
    #큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입, 방문처리
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [], #0노드 없음
  [2,3,8], #1에 연결된 노드 2,3,8
  [1,7], #2에 연결된 노드 1,7
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트). 0부터 8까지 9개
visited = [False] *9 # [False,False,False,False,False,False,False,False,False,]

#정의된 BFS 함수 호출
bfs(graph, 1, visited)