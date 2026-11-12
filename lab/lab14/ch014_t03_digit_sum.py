def digit_sum(n: int):
    sum = 0
    n = str(n)
    for a1 in range(len(n)):
        sum += int(n[a1])
    print(sum)


print(digit_sum(123))
