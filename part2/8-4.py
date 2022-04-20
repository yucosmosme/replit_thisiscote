#p.215
#피보나치 - 동적프로그래밍(반복적, bottom up 방식)으로 해결

#bottomup은 결과 저장용 리스트를 DP테이블이라고 부른다.
d = [0] * 100

#초기값 셋팅
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
	d[i] = d[i-1] + d[i-2]

print(d[n])