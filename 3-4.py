#Shell 탭에서 python 파일명.py로 하면 실행됨
#그리디 1이될때까지 p.99

print('N과 K를 입력하시오. (2<=N,K<=100,000), N은 항상 K보다 크거나 같다.')
N, M = map(int, input().split());
print(N,M);


count = 0;

while N != 1 :
  if N % M == 0 :
    N //= M;
  else :
    N -= 1;
  count += 1;
  print('N: ', N, 'count: ', count);

print('count: ', count)


