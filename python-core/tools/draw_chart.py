import matplotlib.pyplot as plt

data = [1, 3, 2, 5, 25, 24, 5]
labels = list(map(str, data))

red_columns = [1, 6]

# Tạo một mảng màu cho từng cột dữ liệu
colors = ['red' if i in red_columns else 'lightblue' for i in range(len(data))]

# Vẽ biểu đồ cột
plt.bar(range(len(data)), data, tick_label=labels, color=colors)

# Hiển thị biểu đồ
plt.show()
