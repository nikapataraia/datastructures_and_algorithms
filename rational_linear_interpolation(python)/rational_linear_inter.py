import numpy as np
def rational_linear_interpolation(x, y, x_new):
    n = len(x)
    w = np.zeros_like(x)
    for i in range(n):
        d = abs(x[i] - x_new)
        if d == 0:
            return y[i]
        w[i] = 1 / d
    w_sum = np.sum(w)
    w = w.astype(float)
    w /= w_sum
    numerator = np.sum(w * y)
    denominator = np.sum(w)
    return numerator / denominator
