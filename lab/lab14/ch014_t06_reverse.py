def reverse(text: str) -> str:
    #    return text[::-1]
    resultletter = ""
    for lett in text:
        resultletter = lett+resultletter
    return resultletter


print(reverse("HAJIMI"))
