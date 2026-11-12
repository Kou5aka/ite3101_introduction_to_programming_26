def is_prime(x: int):
    if x<=1:
        return False
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


print(is_prime(1))
