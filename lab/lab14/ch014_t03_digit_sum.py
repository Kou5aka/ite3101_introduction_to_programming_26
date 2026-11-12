def digit_sum(n):
    sum = 0
    for a1 in range(len(n)):
        sum += n[a1]
    print(sum)


print(digit_sum(123456))
