#피보나치 재귀로 구현
#이렇게 하면 똑같은 계산을 반복해서 매우 비효율적임
def fibo(x):
	if x == 1 or x == 2:
		return 1
	return fibo(x-1) + fibo(x-2)

print(fibo(99))