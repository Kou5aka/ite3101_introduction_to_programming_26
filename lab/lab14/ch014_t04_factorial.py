def factorial(x: int):
    mult = 1
    for num in range(x):
        mult = mult*(num+1)
    return mult


print(factorial(5))
