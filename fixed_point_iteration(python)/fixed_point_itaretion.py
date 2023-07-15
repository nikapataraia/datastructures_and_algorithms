import math 
import numpy as np
import matplotlib.pyplot as plt

def f(fun,x):
    return fun(x)

def f1(x):
    return (1-x)**(0.2)
def f2(x):
    return ( - math.sin(x) + 5)/6

def f3(x):
    return math.sqrt(3 - math.log(x))


def fpi(fun,starting_cor = 0,interval_len = 5):
    plt.figure(figsize=(8, 6))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('fpi plot')

    a = starting_cor
    b = a
    tol = 10**(-6)
    ismin = fun(a) <= 0
    if(ismin):
        while(fun(b) < 0):
            a = b
            b = b + interval_len
    else:
        while (fun(b) > 0):
            a = b
            b = b + interval_len
    x = np.linspace(a, b, 100)
    plt.plot(x, fun(x), color='blue', label='g(x)')
    plt.plot(x, x, color='gray', linestyle='--', label='f(x) = x')
    x = (b + a)/2
    while(abs(fun(x) - x) > tol): 
        y = fun(x)
        plt.plot([x, x], [x, y], color='black', linestyle='-', linewidth=1)
        plt.plot([x, y], [y, y], color='black', linestyle='-', linewidth=1)
        x = y
    plt.legend()
    plt.show()
    return x

def fpi_prim(fun,x0,tol):
    ite = fun(x0)
    while(abs(ite - x0) > tol):
        x0 = ite
        ite = fun(x0)
    return ite


print(fpi(f1,-5,1))

