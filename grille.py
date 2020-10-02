import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange()
# s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t)

ax.set(xlabel='X', ylabel='Y',
       title='plot')
ax.grid()

fig.savefig("test.png")
plt.show()

