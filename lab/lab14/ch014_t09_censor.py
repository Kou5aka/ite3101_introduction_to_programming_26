def censor(text: str, word: str)-> str:

    result = ""
    num = 0
    for num <= len(text):
        if text[num:num+len(word)] == word:
            text[num:num+len(word)] = "*"*len(word)
            num += len(word)
        else:
            result += text[num]

print(censor("this hack is wack hack", "hack"))