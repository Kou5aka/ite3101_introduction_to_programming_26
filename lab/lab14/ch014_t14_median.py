def median (x:list)->list:
    sorted(x)
    xlen=len(x)
    if xlen%2==0:
        return (x[xlen/2]+x[xlen/2+1])/2
    else:
        return x[xlen//2]