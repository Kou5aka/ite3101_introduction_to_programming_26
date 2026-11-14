def censor (text:str,word:str)—>str:

    result = ""
    num = 0
    for num < len(text):
        if text[num:num+len(word)] == word:
            text[num:num+len(word)] = "*"*len(word)
            i += len(word)
        else:
            text[i]