#Shell 탭에서 python 파일명.py로 하면 실행됨

# CHAPTER 03 그리디 p.92 큰 수의 법칙
# 더해서 가장 큰 숫자는?

# 조건들
# N 배열의 크기
# M 숫자가 더해지는 횟수
# K 같은 인덱스의 값이 연속해서 k 번 초과해서 더해질수없음

print("배열의 크기, 숫자가 더해지는 횟수, 연속해서 초과하여 더할 수 없는 횟수를 공백으로 구분하여 입력하시오.");
N, M, K = map(int, input().split());

# print(N,M,K);

print(N,"개의 수를 공백으로 구분하여 입력하시오");
data = list(map(int, input().split())); #배열 형태 ex. [3,4,5]

# print(data);

data.sort(); #배열 정렬

first = data[N-1]; # 제일 큰 수
second = data[N-2]; #두번째로 큰 수

firstCount = M // K; # 도는 횟수
print('first', first)
print('second', second)
print('firstcount: ',firstCount)
secondCount = M - (firstCount * K);
print('secondCount: ', secondCount)

result = first * firstCount * K + second * secondCount

print("결과는 ", result, " 입니다.")



