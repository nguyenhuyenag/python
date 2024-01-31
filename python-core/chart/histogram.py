import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(1000)

plt.hist(data, bins=30, edgecolor='black')

plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
