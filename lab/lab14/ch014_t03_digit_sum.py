def digit_sum(n: int):
    sum = 0
    n = str(n)
    for a1 in range(len(n)):
        sum += int(n[a1])
    return sum



def digit_sum2(n:int):
    sum=0
    for a2 in range(len(n)):