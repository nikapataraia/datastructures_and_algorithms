import numpy as np


def w(xall, j):
    w = 1
    for k in range(len(xall)):
        if (j != k):
            w = w * (xall[j] - xall[k])
    return 1/w

def barycentric(xall, yall, x):
    top = 0
    for ind in range(len(np.array(xall))):
        top = top + (w(xall, ind) * yall[ind])/(x - xall[ind])
    bot = 0
    for ind in range(len(np.array(xall))):
        print(xall)
        bot = bot + (w(xall, ind))/(x - xall[ind])
    return top/bot
