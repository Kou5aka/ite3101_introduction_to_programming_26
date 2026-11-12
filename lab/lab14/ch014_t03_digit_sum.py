def digit_sum(n: int):
    sum = 0
    n = str(n)
    for a1 in range(len(n)):
        sum += int(n[a1])
    return sum


def digit_sum2(n: int):
    sum = 0
    for a2 in range(len(str(n))):
        sum += n//(10*a2)
    return sum


print(digit_sum2(12))
