#p.132 팩토리얼을 재귀함수로 구현

#반복적으로 구현한 n!
def factorial_iterative(n):
  result = 1;
  for i in range(1, n+1):
    result *= i;
  return result;

#재귀함수를 이용한 n!
def factorial_recursive(n):
  if n <= 1 : #1보다 작을때 조건문 넣는거 필수임
    return 1;
  return n * factorial_recursive(n-1);


#결과 출력
print(factorial_iterative(3));
print(factorial_recursive(3));

