def censor(text: str, word: str) -> str:

    result = []
    for s in text.split():
        if s == word:
            result.append("")


#print(censor("this hack is wack hack", "hack"))
