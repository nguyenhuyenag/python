# import matplotlib.pyplot as plt
#
# data = [1, 3, 2, 5, 25, 24, 5]
# labels = list(map(str, data))
#
# red_columns = [1, 6]
#
# # Tạo một mảng màu cho từng cột dữ liệu
# colors = ['red' if i in red_columns else 'lightblue' for i in range(len(data))]
#
# # Vẽ biểu đồ cột
# plt.bar(range(len(data)), data, tick_label=labels, color=colors)
#
# # Hiển thị biểu đồ
# plt.show()


import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Dữ liệu cho biểu đồ
data = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Tạo nhãn từ dữ liệu
labels = list(map(str, data))

# Xác định vị trí các cột cần tô màu đỏ
red_columns = [1, 8]

# Tạo danh sách màu sắc cho mỗi cột dựa trên vị trí của chúng
colors = ['red' if i in red_columns else 'lightblue' for i in range(len(data))]

# Tạo một figure và trục
fig, ax = plt.subplots()

# Vẽ biểu đồ cột với màu sắc tương ứng
ax.bar(range(len(data)), data, tick_label=labels, color=colors)

# Tọa độ cho hình chữ nhật màu xanh dương
x1 = 2
x2 = len(data)
y1 = 0
y2 = data[-1]

# Tạo hình chữ nhật từ tọa độ x1, y2 với chiều rộng và chiều cao tương ứng
# Lưu ý: phải trừ 0.5 từ x1 và x2 để hồi chữ nhật không che khuất cột thứ 3 và cột cuối cùng
rectangle = patches.Rectangle((x1-0.5, y1), x2-x1, y2, linewidth=1, edgecolor='blue', facecolor='blue', alpha=0.2)

# Thêm hình chữ nhật vào trục
ax.add_patch(rectangle)

# Hiển thị biểu đồ
plt.show()
