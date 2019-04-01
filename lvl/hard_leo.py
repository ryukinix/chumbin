# coding: utf-8

import numpy as np
from matplotlib import pyplot as plt
import math

e = 1
lvl_max = 10
m = -100
xp_max = 1000
xp_factor = 1/(xp_max/50)


def lvl(x):
    return m/(e*(x*xp_factor + lvl_max)) + lvl_max

x = np.linspace(1, 1000, 1000)
y = np.vectorize(lambda x: lvl(x))
# y2 = np.vectorize(lambda x: lvl2(x))
plt.close('all')
plt.plot(x, y(x))
# plt.plot(x, y2(x), color='r')
ax = plt.gca()
ax.set_title("SISTEMA DE LEVEL: HARD LEO")
ax.set_xlabel("XP")
ax.set_ylabel("LEVEL(XP)")
plt.show(block=False)
