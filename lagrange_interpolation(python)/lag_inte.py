import numpy as np

x_data = [1,2,3,4,5,6]
y_data = [1,2,3,5,7,10]

def lag_inte(x,x_da,y_da):
    res = 0
    length = len(x_da)
    if(length != len(y_da)):
        Exception("lol")
    for i in range(length):
        l = 1
        for j in range(length):
            if(i != j):
                l = l * ((x-x_da[j])/(x_da[i]-x_da[j]))
        res = res + l * y_da[i]
    return res

