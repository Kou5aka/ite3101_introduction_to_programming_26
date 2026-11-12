def is_prime (x:int):
    for n in range(x-1):
        if x%n==0:
            return False
        else:
            retirm True
            