import matplotlib.pyplot as plt
import numpy as np
from dtw import dtw

x = np.array([2, 0, 1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)
y = np.array([1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)

plt.plot(x, label='x')
plt.plot(y, label='y')
plt.title('Our two temporal sequences')
plt.legend()

l2_norm = lambda x, y: (x - y) ** 2
dist, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=l2_norm)

plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
plt.plot(path[0], path[1], 'w')
plt.show()
