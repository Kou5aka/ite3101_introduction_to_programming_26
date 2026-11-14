def product (x:list)->int:
    result = 1
    for num in x:
        result = result*num
    return result

print(product([1,3,5,4,4]))