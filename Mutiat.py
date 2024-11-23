import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Collins", "Blake", "Nulu", "Steph"])
y = np.array([4, 13, 5,9])

plt.bar(x,y, color = "green")
plt.show()