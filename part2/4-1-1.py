#Shell 탭에서 python 파일명.py로 하면 실행됨
#구현 상하좌우 p.110

print('공간의 크기를 입력하시오. 1<=N<=100');
N = int(input());
print('N:', N);

print('여행가 A의 이동계획서를 입력하시오. L,R,U,D중 1<=이동횟수<=100의 조건으로 공백 기준으로 입력.');
list = input().split();
print('list:', list)

#좌표: 앞에꺼가 행 뒤에꺼가 열
position = [1,1];

for i in list :
  if i == "R": 
    if position[1] < N :
      position[1] += 1;
  
  elif i == "D" :
    if position[0] < N :
      position[0] += 1;
    
  elif i == "U" :
    if position[0] > 1 :
      position[0] -= 1;
  
  elif i == "L": 
    if position[1] > 1 :
      position[1] -= 1;


print('position:', position);