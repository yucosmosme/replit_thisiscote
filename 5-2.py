#큐 p.129
from collections import deque

queue = deque() #빈 큐 생성

queue.append(5)
queue.append(2)
queue.append(7)
queue.popleft() #이건 선입선출(큐 방식)
#queue.pop() #이건 선입후출 (스택 방식)
print(queue)
queue.reverse() #순서 바꾸기
print(queue)