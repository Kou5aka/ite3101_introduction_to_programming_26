def censor(text: str, word: str) -> str:

    result = ""
    num = 0
    for num in range(len(text)):
        if text[num:num+len(word)] == word:
            result += "*"*len(word)
         #   num += len(word)
        else:
            result += text[num]
    return result


print(censor("this hack is wack hack", "hack"))
