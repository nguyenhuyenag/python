# http://www.cse.net.vn/python/plot.html#1
# pip install matplotlib
# note run as admin
import matplotlib.pyplot as plt

x = [2, 6, 8, 8, 12, 16, 20, 20, 22, 26]
y = [58, 105, 88, 118, 117, 137, 157, 169, 149, 202]
x1 = [0, 26]
y1 = [60, 190]
plt.scatter(x, y, color='g')
plt.plot(x1, y1)
plt.show()
