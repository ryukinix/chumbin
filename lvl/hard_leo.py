# coding: utf-8

import numpy as np
from matplotlib import pyplot as plt
import math

e = 1
l_max = 10
m = -1

def lvl(x):
    return -1/x + l_max


def lvl2(x):
    return (m - l_max)/(e*x + l_max) + (l_max + 0.1)


x = np.linspace(11, 100, 1000)
y = np.vectorize(lambda x: lvl(x))
y2 = np.vectorize(lvl2)
plt.close('all')
plt.plot(x, y(x))
plt.plot(x, y2(x), color='r')
ax = plt.gca()
ax.set_title("SISTEMA DE LEVEL: HARD LEO")
ax.set_xlabel("XP")
ax.set_ylabel("LEVEL(XP)")
plt.show(block=False)
