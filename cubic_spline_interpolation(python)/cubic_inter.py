import numpy as np

def cubic_interpolation(x, y, x_new):
    n = len(x)
    if len(y) != n:
        raise ValueError("x and y must have the same length")
    h = np.diff(x)
    delta = np.diff(y) / h
    alpha = np.zeros(n)
    for i in range(1, n-1):
        alpha[i] = 3(delta[i] - delta[i-1]) / (h[i] + h[i-1])

    l, mu, z = np.zeros(n), np.zeros(n), np.zeros(n)
    l[0] = 1
    mu[0] = z[0] = 0
    for i in range(1, n-1):
        l[i] = 2(x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1]*z[i-1]) / l[i]

    l[n-1] = 1
    z[n-1] = 0
    c, b, d = np.zeros(n), np.zeros(n), np.zeros(n)

    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = delta[j] - h[j]*c[j+1]
        d[j] = (c[j+1] - c[j]) / (3*h[j])
    y_cubic = np.zeros_like(x_new)
    for i, x_val in enumerate(x_new):
        index = np.searchsorted(x, x_val)

        if index == 0:
            index = 1
        elif index == n:
            index = n - 1

        h_i = x[index] - x[index-1]
        t = (x_val - x[index-1]) / h_i

        y_cubic[i] = y[index-1] + b[index-1]*t + c[index-1]*(t**2) + d[index-1]*(t**3)
    return y_cubic
