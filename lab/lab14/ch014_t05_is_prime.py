def is_prime(x: int):
    if x<=
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


print(is_prime(1))
