#Shell 탭에서 python 파일명.py로 하면 실행됨
# p.96 숫자카드게임

#print('카드 행의 개수 N과 열의 개수 M을 공백을 기준으로 자연수로 입력하시오. (1<=N,M<=100) ')
#N, M = map(int, input().split());
#temp = input().split();
temp = [];
N = 0;
M = 0;

#입력받을때 while문 돌려서 조건에 안맞으면 다시 입력받기
while (1) :

  print('카드 행의 개수 N과 열의 개수 M을 공백을 기준으로 자연수로 입력하시오. (1<=N,M<=100) ')
  temp = input().split();

  if len(temp) == 2 :
    #실수입력했을때 정수로 바꿔주기
    N, M = map(float, temp);
    print(type(N))
    N = int(N); 
    M = int(M);
    print(type(N))
    break;
  else :
    print('공백기준으로 2개의 숫자를 입력하세요.');

print('N: ', N, 'M: ', M);

#배열 선언
arr = [];

#N행만큼 포문 돌리고 M개만큼 입력받아서 배열에 저장
for i in range(N):
  print(M,'개의 자연수를 공백 기준으로 입력하시오. 1이상 10,000이하');
  #arr[i] = map(int, input().split());
  arr.append(list(map(int, input().split())));

print(arr);

minValue = 10001;

for i in arr:
  if minValue > min(i): 
    minValue = min(i);

print(minValue);

