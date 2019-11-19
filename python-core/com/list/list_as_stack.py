# Sử dụng list như ngăn xếp (last in, first out)
queue = [1, 2, 3]
queue.append(4)
queue.append(5)

while len(queue) > 0 :
    print(queue.pop())
