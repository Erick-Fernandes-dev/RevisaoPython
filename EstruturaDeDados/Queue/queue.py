from collections import deque

minha_queue = deque()
minha_queue.append(5)
minha_queue.append(10)
minha_queue.append(15)
minha_queue.append(20)



print(minha_queue)
print(minha_queue.popleft())
print(minha_queue.popleft())
print(minha_queue.popleft())
