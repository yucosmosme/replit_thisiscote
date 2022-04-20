# 구현 상하좌우 p.110
# 교재에 나온 답

n = int(input());
x, y = 1, 1
plans = input().split();

dx = [0,0,-1,1]; # 행 위 아래 이동
dy = [-1,1,0,0]; # 열 좌 우 이동
move_types = ['L', 'R', 'U', 'D'];

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]; # L일경우 nx = 1 + 0 = 1, R일경우 nx = 1 + 0 = 0, U일 경우 nx = 1 + -1 = 0;
      ny = y + dy[i];
  #공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(x,y)