def median (x:list)->list:
    sorted(x)
    xlen=len(x)
    if xlen%2==0:
        x[xlen]