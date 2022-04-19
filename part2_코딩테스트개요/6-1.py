#p.159 선택정렬

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): #한번 정렬할때마다 정렬 길이 줄어듦
  min_index = i #가장 작은 원소의 인덱스. 첫번째 0부터 시작
  for j in range(i+1, len(array)): #계속 포문돌면서 두개 비교해서 더작은거를 min_index로 계속 바꿔줌 (정렬)
    if array[min_index] > array[j]:
      min_index = j  # 더 작은거 인덱스 바꿔놓음

  #스와핑. 두 변수의 위치를 교환. 파이썬에서는 이렇게 간단히 할수있음
  array[i], array[min_index] = array[min_index], array[i]

print(array)