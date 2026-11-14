def median(x: list):
    x=sorted(x)
    midex = len(x)
    if xlen % 2 == 0:
        return (x[xlen//2]+x[xlen//2-1])/2
    else:
        return x[len(x)//2]


print(median([5, 2, 1, 4, 3]))
