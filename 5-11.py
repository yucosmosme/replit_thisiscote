#p.152 dfs, bfs 연습 
#미로탈출
#bfs가 효과적: 시작에서 가까운 노드부터 차례대로 모든 노드를 탐색하기 때문

from collections import deque

print('미로의 세로길이 n과 가로길이 m을 입력하시오. (4<=n,m<=200)')
n,m = map(int, input().split())

graph = []

for i in range(n):
  print(m,'개의 미로 정보를 입력하시오. 괴물있는칸 0, 아닌칸 1')
  graph.append(list(map(int, input().split())));
  
print(graph)


#이동방향 정의(상하좌우)
#for문돌리려면 아래와같이 정의한다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

  #큐생성
  queue = deque();
  #큐에 추가 : 첫번째 위치(0,0)는 항상 1이라고 가정하기 때문에 바로 큐에 넣어도 된다.
  queue.append((x,y))
  
  #큐가 빌때까지 반복
  while queue:
  
    #큐에서 현재위치 뽑아서
    x, y = queue.popleft()
    print(x,y)
    
    #현재위치에서 네 방향 위치 확인
    for i in range(4):
      nx = x + dx[i] 
      ny = y + dy[i]

      #미로 벗어나면 안됨
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      #괴물있으면 안됨
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        #그전 위치의 값에 계속 +1을 해줌으로써 이동횟수 계산
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny)) #큐추가
      
  return graph[n-1][m-1] #마지막위치는 항상 1이니까 마지막 위치에서의 값(이동횟수) 리턴
  
print(bfs(0,0)) #미로 (0,0)~(n-1, m-1)까지