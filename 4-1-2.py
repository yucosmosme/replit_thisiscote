#Shell 탭에서 python 파일명.py로 하면 실행됨

print('정수 N을 입력하시오. (0<=N<=23)')
N = int(input());
print('N',N);

MM = 60;
SS = 60;
HHMMSS = '';
count = 0;

for hh in range (0, N+1) :
  for mm in range (0, MM) :
    for ss in range (0, SS) :
      HHMMSS = str(hh) + str(mm) + str(ss);
      if HHMMSS.find('3') >= 0 :
        print('HHMMSS', HHMMSS) ;
        count += 1; 

print('count:', count);
