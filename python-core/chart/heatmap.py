import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = np.random.rand(10, 10)

sns.heatmap(data, annot=True)
plt.title('Heatmap')
# plt.xlabel('Categories')
# plt.ylabel('Values')
plt.show()
