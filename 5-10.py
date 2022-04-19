#p.149 DFS/BFS 음료수얼려먹기
#0 1을 스택의 방문처리로 쓰면된다.

print('얼음틀의 세로길이 n과 가로길이 m을 입력하시오. (1<=n,m<=1000)')
n,m = map(int, input().split())

graph = []

for i in range(n):
  print(m,'개의 얼음틀의 형태를 입력하시오. 구멍뚫린부분 0, 아닌부분 1')
  graph.append(list(map(int, input().split())));

print(graph)

def dfs(x, y):

  #주어진 범위를 벗어나는 경우에는 즉시 종료
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
    
  #현재 노드를 방문하지 않았다면
  if graph[x][y] ==0:
    #print('0인 x,y', x,y )
    #해당노드 방문처리
    graph[x][y] = 1
    #상하좌우 위치도 재귀적으로 호출
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    #print('return true x y:',x,y)
    return True
  return False


#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    #print('i, j:', i, j)
    if dfs(i, j) == True:
      result += 1
      #print('result:::', result)

print(result)