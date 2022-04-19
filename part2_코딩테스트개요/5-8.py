#p.142 DFS 예제

#DFS는 스택이용. 재귀함수로 이용하면 간결하게 구할수있다.

#DFS 메서드 정의

#v는 현재노드
def dfs(graph, v, visited):
  #현재 노드를 방문처리
  visited[v] = True
  print(v, end=' ') #end: 프린트간 개행을 없애줌
  #print('현재노드',v)
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문
  #방문이 끝나고 갈데가 없으면 그 재귀 부른 전 노드로 돌아가고 거기서도 갈게 없으면 그 전꺼로 계속 돌아가서 처음으로 돌아가면 끝이 나는듯??
  for i in graph[v]:
    #print('연결노드',i)
    if not visited[i]:
      #print('방문안함',i,'호출')
      dfs(graph, i, visited)
    

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

#정의된 DFS 함수 호출
dfs(graph, 1, visited)