def median(x: list):
    x = sorted(x)
    midex = len(x)
    if xlen % 2 == 0:
        return (x[midex//2]+x[midex//2-1])/2
    else:
        return x[midex//2]


print(median([5, 2, 1, 4, 3]))
