def is_prime(x: int):
    for n in range(2, x-1):
        if x % (n+1) == 0:
            return False
        else:
            return True


#print(is_prime(222))
