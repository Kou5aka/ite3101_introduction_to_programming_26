def anti_vowel (text:str):
    VOWEL="AIUEOaiueo"
    result=""
    for lett in text:
        if lett not in VOWEL:
            result +=lett
    return result
