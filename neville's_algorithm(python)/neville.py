def neville(datax, datay, x):
    n = len(datax)
    p = n[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
            else:
                p[i] = ((x-datax[i+k])* p[i] + (datax[i]-x)*p[i+1]) / (datax[i]-datax[i+k])
    return p[0]
