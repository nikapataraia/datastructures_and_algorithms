import numpy as np 


def polyfit(x, y, degree):
    # Check if x and y have the same length
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")

    # Check if degree is a non-negative integer
    if not isinstance(degree, int) or degree < 0:
        raise ValueError("degree must be a non-negative integer")

    n = len(x)
    m = degree + 1

    # Create the Vandermonde matrix
    X = [[x_val ** i for i in range(m)] for x_val in x]

    # Transpose the Vandermonde matrix
    XT = [[X[j][i] for j in range(n)] for i in range(m)]

    # Compute the product of XT and X
    XTX = [[sum(XT_row[k] * X_col[k] for k in range(n))
            for X_col in XT] for XT_row in X]

    # Compute the product of XT and y
    XTy = [sum(XT_row[i] * y_val for i, y_val in enumerate(y))
           for XT_row in XT]

    # Solve the linear system (XTX * coefficients = XTy)
    coefficients = gauss_elimination(XTX, XTy)

    return coefficients


def gauss_elimination(A, b):
    n = len(A)

    # Augment A with b
    augmented = [A[i] + [b[i]] for i in range(n)]

    # Forward elimination
    for i in range(n):
        pivot = augmented[i][i]
        if pivot == 0:
            raise ValueError(
                "Cannot perform Gaussian elimination: singular matrix")
        for j in range(i + 1, n):
            factor = augmented[j][i] / pivot
            for k in range(i, n + 1):
                augmented[j][k] -= factor * augmented[i][k]

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = augmented[i][n]
        for j in range(i + 1, n):
            x[i] -= augmented[i][j] * x[j]
        x[i] /= augmented[i][i]

    return x

def pade_approximation(f, x_data, m, n):
    y_data = f(x_data)
    numerator_coeffs = np.polyfit(x_data, y_data, m)
    y_data_rat = y_data / np.polyval(numerator_coeffs, x_data)
    denominator_coeffs = np.polyfit(x_data, y_data_rat, n)
    if denominator_coeffs[-1] < 0:
        numerator_coeffs = -numerator_coeffs
        denominator_coeffs = -denominator_coeffs
    return lambda x: np.polyval(numerator_coeffs, x) / np.polyval(denominator_coeffs, x)

def f(x):
    return x**2 + x**6 - x**7  +1

x = np.array([1,2,3])
print(pade_approximation(f,x,15,4)(3))