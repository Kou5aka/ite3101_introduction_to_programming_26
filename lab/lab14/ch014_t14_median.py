def median(x: list):
    x = sorted(x)       #排序并创建新list
    midnum = len(x)//2  #中位数字
    if len(x) % 2 == 0:
        return (x[midnum]+x[midnum-1])/2
    else:
        return x[midnum]


print(median([5, 2, 1, 4, 3]))
