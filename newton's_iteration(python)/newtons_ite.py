import numpy as np

def fu(x):
    return x**2 + x *2 -1
def derivative(f,x,h):
    return (f(x+h) - f(x-h))/(2*h)

def newton_ite(f,x,tol):
    if(f(x) != 0):
        isneg = f(x) < 0
        while(isneg == (f(x) < 0)):
            x = x + 1
            if(f(x) == 0):
                return x
        xn = x - 0.5
        xnn = xn - (f(xn))/derivative(f,xn,0.1)
        while(abs(xn - xnn) > tol):
            xn = xnn
            xnn = xnn - f(xnn)/derivative(f,xnn,0.1)
        return xnn
    else :
        return x
    


