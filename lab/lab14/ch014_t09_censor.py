def censor (text:str,word:str)—>str:

    result = ""
    num = 0
    for  < len(text):
        if text[i:i+len(word)] == word:
            text[i:]