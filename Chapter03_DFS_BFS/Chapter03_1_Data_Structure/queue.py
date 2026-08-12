# 큐를 쓰려면 라이브러리를 써야 함.
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse() # 역순으로 바꿔주기
print(queue)

queue = list(queue)
print(queue) # 리스트로 변환하기