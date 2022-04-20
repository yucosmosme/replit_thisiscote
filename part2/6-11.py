#p.181
#학생이름:점수를 점수기준으로 오름차순
#튜플방식

import operator #튜플을 operator 사용하여 정렬

n = int(input('input students count n'))
print(n)

list = {} #딕셔너리: {'mimi':3, 'nini':7} 이런 형태

for i in range(n):
	print(i)
	info = input('input name and grade. 0<=grade<=100').split()
	list[info[0]]=int(info[1])

print(list)


#list.items()는 key기준 정렬
#list.key()는 key만정렬
#key=operator.itemgetter(1),붙이면 value기준정렬
#아래는 오퍼레이터 기준으로 정렬기준key값을 넣어주는방법
#newlist = sorted(list.items(),  key=operator.itemgetter(1), reverse=True)

#아래는 람다함수를 사용하여 정렬기준key값을 넣어주는 방법
#x는 해당 {name:grade} 쌍으로 x[0]을 넣으면 이름, x[1]이면 점수를 넣어줘서 그 기준으로 정렬하게 된다.
newlist = sorted(list.items(), key=lambda x: x[0])

print(newlist)
