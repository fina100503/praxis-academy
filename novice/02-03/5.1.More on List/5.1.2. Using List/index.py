from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()
print(queue.popleft()) 
queue = deque(["Eric", "John", "Michael"]) 
queue.append("Terry")
queue.append("Graham")
queue.popleft()
print(queue.popleft())
queue
print(queue)  
