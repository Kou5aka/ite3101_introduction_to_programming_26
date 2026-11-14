def censor (text:str,word:str)—>str:

    result = ""
    num = 0
    for num < len(text):
        if text[num:i+len(word)] == word:
            text[i:]