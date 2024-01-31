import matplotlib.pyplot as plt

lables = ['A', 'B', 'C']
sizes = [30, 45, 25]

plt.pie(sizes, labels=lables, autopct='%1.1f%%')
plt.title('Pie chart')
# plt.xlabel('Categories')
# plt.ylabel('Values')
plt.show()
