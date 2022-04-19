#Shell 탭에서 python 파일명.py로 하면 실행됨

# 왕실의 나이트. p.115
# 푼 날짜: 2022.03.12 걸린 시간: 50분 
import operator #튜플 간 덧샘뻴셈하는 용

# 나이트가 움직일 수 있는 경로 모음
steps = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)];

print('a1~h8 중 하나를 입력하시오.');
knight = input(); #ex. a1
string = list(knight); #글자를 하나씩 쪼갬
knightFirst = ord(string[0]) - 96; #첫번째 알파벳 글자를 숫자로 바꿔주는 방법

knight = (knightFirst, int(string[1])); # (1, 1) 이런 튜플 형태로 바꿔줌
print('knight', knight);

#이동 가능한 경로 수
count = 0;

for i in steps:
  #print(type(i)); #(1,1)이런건 튜플 타입
  #튜플 간 더하기
  afterKnight = tuple(map(operator.add, i, knight));   print('afterKnight', afterKnight);
  print('afterKnight', afterKnight[0]); #수평 
  print('afterKnight', afterKnight[1]); #수직
  #이동후에 수직 수평 위치 모두 0보다 크고 8보다 작아야 이동 가능한 경로에 포함된다.
  if (afterKnight[0] > 0) and (afterKnight[1] > 0) and (afterKnight[0] < 9) and (afterKnight[1] < 9) :
    count += 1;
    
print('count:', count);



