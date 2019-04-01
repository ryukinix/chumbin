from math import log
import numpy as np
from matplotlib import pyplot as plt


plt.close('all')
c = abs(-1.98412 - 0.644771j)
k = 1/log(c)
vec_log = np.vectorize(lambda xp: log(xp + c))
xp = np.linspace(0, 1560, 100)
lvl = k * vec_log(xp)


# plt.scatter(xp_sample, lvl_sample, color='r')
plt.plot(xp, lvl)
ax = plt.gca()
ax.set_title("SISTEMA DE LEVEL: HARD")
ax.set_xlabel("EXPERIENCIA (XP)")
ax.set_ylabel("LEVEL (LVL)")
plt.savefig("../pics/hard.png")
plt.show(block=False)
