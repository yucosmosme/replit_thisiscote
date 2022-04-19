#p.118 
#4-3 게임개발
#2022-03-13 14:30시작

n,m = map(int, input('맵의 세로 크기 n과 가로크기 m을 공백을 구분하여 입력하시오. (3<=N,M<=50)').split());
print('n,m: ',n,m);

#방문한 위치를 저장하기 위한 맵 0으로 초기화
#for _ in range()는 리턴값 i가 필요없을때
d = [[0] * m for _ in range(n)];
print('d', d);

x,y,direction = map(int, input('게임 캐릭터가 있는 좌표(A,B)와 바라보는 방향 d를 공백으로 구분하여 입력하시오. 방향 d로는 0북쪽, 1동쪽, 2남쪽, 3서쪽 이 네가지가 있다.').split());
print('x,y,direction', x,y,direction);
d[x][y] = 1 # 현재 좌표는 방문한 걸로 처리

# 전체 맵의 육지0 바다1 여부
array = [];

for i in range(n) :
  print(m,'개의 맵이 육지인지 바다인지 공백 기준으로 입력하시오. 0육지 1바다');
  #######중요!!!array에 append이므로 list()로 감싸줘야 한다!!!!!!!!!!!!!!!!!!!
  array.append(list(map(int, input().split()))); # 리스트 안에 리스트가 들어간다.
print('array:', array);
array[x][y] = 0 # 현재 좌표는 육지로 처리

#서북동남 으로 이동하는 경우 정의
dx = [-1,0,1,0]; # 서쪽 동쪽 이동할때
dy = [0,1,0,-1]; # 남쪽 북쪽 이동시

#반시계방향으로 -90도씩 회전하는 함수 정의
def turn_left():
  global direction; 
  direction -= 1;
  if direction == -1 : # 북쪽에서 서쪽으로 이동시
    direction = 3;

#시뮬레이션 시작
count = 1 #캐릭터가 방문한 칸의 수 (현재칸방문한거니까 1로 초기화)
turn_time = 0 # 4번 회전했는데 모두 가본칸이거나 바다일 경우 바라보는 방향을 유지한채 한칸 뒤로 가야함. 이 때도 바다라 뒤로 갈수 없으면 움직임을 멈춤

while True:
  #왼쪽으로 회전 먼저 한다.
  turn_left()
  
  #회전한 방향으로 1보 전진한 임시 위치 nx, ny
  nx = x + dx[direction]
  ny = y + dy[direction]
  
  #####회전했는데 정면이 가본적없고 육지일 경우 1보 전진
  if d[nx][ny] == 0 and array[nx][ny] == 0: 
    d[nx][ny] = 1 # 해당위치 가본적 있음으로 변경
    x = nx; # 해당위치 실제 위치로 주입
    y = ny; # 실제 위치로 주입
    count += 1; # 방문한 칸 1 증가\\\\\\\\\
    turn_time = 0; #회전 횟수 초기화
    continue  # 이후에 나오는 코드들을 무시한다.
    
  #####회전한 이후에 정면이 가봤거나 바다일경우 회전만
  else :
    turn_time += 1 # 회전횟수 1 증가 (4번 하면 뒤로 1보해야되니까)

  #사면이 다 가본 데라면 뒤로 1보    
  if turn_time == 4 :  
    nx = x - dx[direction]
    ny = y - dy[direction]
    if array[nx][ny] == 0 : #육지면 실제로이동
      x = nx
      y = ny
    else : #바다면 멈춤
      break
    turn_time = 0 # 바다가 아닐 경우에 회전수를 0으로 초기화해야 함. 다시 루프 처음으로 돌아갔을때 이동 가능할 경우 이동을 해야 하니까..

#정답 출력
print('count',count)
        
    
    
    
    
  