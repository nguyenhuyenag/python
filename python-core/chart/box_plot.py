import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

sns.boxplot(data=data)
plt.title('Box plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
