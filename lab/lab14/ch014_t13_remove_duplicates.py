def remove_duplicates(x: list) -> list:
    result = []
    for num in x:
        if num not in result:
            result.append(num)
    return result


print(remove_duplicates([1, 1, 2, 2]))
