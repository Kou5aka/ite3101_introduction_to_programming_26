def censor(text: str, word: str) -> str:

    result = ""
    num = 0
    while num < range(len(text)):
        if text[num:num+len(word)] == word:
            result += "*"*len(word)
            num += len(word)
        else:
            result += text[num]
            num += 1
    return result


print(censor("this hack is wack hack", "hack"))
