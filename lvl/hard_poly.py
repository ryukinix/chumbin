# coding: utf-8

import numpy as np
from matplotlib import pyplot as plt
import math

c = 100
b = 1 + 0.007 + 18
amp = 10 # 1000 + 85
m = 1 # 10


def lvl(x):
    return amp*(((m*x + 300) - c) / (2 * c - (m*x + 300))) + b


x = np.linspace(1, 999, 100)
y = np.vectorize(lambda x: lvl(math.floor(x)))
plt.close('all')
plt.plot(x, y(x))
ax = plt.gca()
ax.set_title("SISTEMA DE LEVEL: HARD POLY")
ax.set_xlabel("XP NECESSÁRIA PARA SUBIR AO PRÓXIMO NÍVEL")
ax.set_ylabel("LEVEL(XP)")
plt.show(block=False)
