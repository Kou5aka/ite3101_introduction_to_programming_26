def median(x: list):
    x = sorted(x)
    midinde = len(x)//2
    if len(x) % 2 == 0:
        return (x[midex]+x[midex-1])/2
    else:
        return x[midex]


print(median([5, 2, 1, 4, 3]))
