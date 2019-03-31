#!/usr/bin/env python
# coding: utf-8


import numpy as np
from matplotlib import pyplot as plt
from math import sqrt

xp_sample = np.array(
    [0, 50, 200, 500, 600, 780, 900, 1200, 1400, 1500]
)
lvl_sample = np.array(range(1, 10+1))


x = xp_sample
y = lvl_sample


y_mean = np.mean(y)
x_mean = np.mean(x)
beta_1 = (sum(x*y) - y_mean*sum(x)) / (np.sum(x * x) - x_mean * sum(x))
beta_0 = y_mean - beta_1 * x_mean

y_pred = beta_0 + beta_1 * x

syy = sum(y - np.mean(y))
r2 = 1 - (sum((y - y_pred) ** 2) / sum((y - y_mean) ** 2))
rmse = sqrt(sum((y - y_pred) ** 2)/len(x))
print(__doc__)
print("RESULTS")
print("-------")
print("RMSE: ", rmse)
print("R2: ", r2)
print("B0: ", beta_0)
print("B1: ", beta_1)
print(f"EQ: Ŷ(x) = {beta_0:.2f}  + {beta_1:.2f}*x")
print(f"")
plt.close('all')
plt.scatter(x, y, color='r')
plt.plot(x, y_pred)
ax = plt.gca()
ax.set_title("SISTEMA DE LEVEL: NORMAL")
ax.set_xlabel("EXPERIENCIA (XP)")
ax.set_ylabel("LEVEL (LVL)")
plt.show(block=False)
plt.savefig("../pics/normal.png")
