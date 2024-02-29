import heapq

"""
    heapq: Sử dụng một list có sẽ để làm heap. Phần tử nhỏ sẽ được ưu tiên
"""

# Một danh sách không sắp xếp
data = [3, 5, 1, 2, 6, 8, 7]


def heapify():
    # Chuyển danh sách thành heap
    heapq.heapify(data)
    print("Heap sau khi heapify:", data)


"""
    heappush(): Thêm phần tử mới vào heap
"""
def heappush():
    heapq.heappush(data, 0)
    print("Heap sau khi thêm 0:", data)


"""
    heappop(): Lấy ra và xóa phần tử nhỏ nhất 
"""
def heappop():
    print("Phần tử nhỏ nhất đã bị loại bỏ:", heapq.heappop(data))
    print("Heap sau khi loại bỏ:", data)


"""
    Thêm mới + lấy ra và xóa phần tử nhỏ nhất
        heappushpop(list, x) = {
            heappush(list, x)
            return heappop(list)
        }
"""
def heappushpop():
    print("Phần tử mới thêm và phần tử nhỏ nhất:", heapq.heappushpop(data, 8))

"""
    Lấy ra và xóa phần tử nhỏ nhất + thêm mới
        heapreplace(): = {
            top = heappop(list)
            heappush(list, x)
            return top
        }
"""
def heapreplace():
    replace_min_element = heapq.heapreplace(data, 7)
    print("Phần tử nhỏ nhất đã bị loại bỏ và phần tử mới thêm vào:", replace_min_element)
    print("Heap sau khi loại bỏ và thêm:", data)

if __name__ == '__main__':
    heapify()
    # heappush()
    # heappop()
    # heappushpop()
    heapreplace()
