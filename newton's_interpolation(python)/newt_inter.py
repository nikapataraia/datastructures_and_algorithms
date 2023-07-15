import numpy as np
import matplotlib.pyplot as plt


def coef(x, y):
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):

        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])

    return np.array(a) 


def newt_inter(a, x, r):
    n = len(a) - 1
    temp = a[n] + (r - x[n])
    for i in range(n - 1, -1, -1):
        temp = temp * (r - x[i]) + a[i]
    return temp


x = [1, 2, 3, 4, 5,6]
y = [1, 3, 6, 10, 12,20]
print(newt_inter(coef(x,y),x,5.001))