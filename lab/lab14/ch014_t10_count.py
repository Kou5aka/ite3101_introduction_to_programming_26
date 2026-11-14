def count(sequence, item):
    times = 0
    for a in sequence:
        if item == sequence[a]:
            times+=1
    return times

print(count())