def count(sequence, item):
    times = 0
    for a in sequence:
        if a == item:
            times += 1
    return times


print(count([1, 2, 1, 1, 2, 2, 2], 2))
