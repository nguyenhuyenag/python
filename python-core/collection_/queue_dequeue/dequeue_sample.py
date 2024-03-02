from collections import deque

"""
    deque(): Hàng đợi 2 đầu
"""
q = deque()

for i in range(5):
    q.append(i)
    q.appendleft(i)

print("Initial queue:", q)
print("\nElements dequeued from the queue")
print("pop(): ", q.pop())
print("popleft(): ", q.popleft())
# print(q.copy())
print("count(2): ", q.count(2))
print("index(3): ", q.index(3))
q.insert(2, 2024)
q.rotate(3)

# print(q.clear())

print("\nQueue after removing elements")
print(q)
