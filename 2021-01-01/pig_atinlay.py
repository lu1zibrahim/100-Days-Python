def pig_latin(word):
    if len(word) > 3:
        return word[1:] + word[0] + "ay"
    else:
        return word


#Another way
"""def pig_latin(word):
    return word[1:]+word[0]+'ay' if len(word)>3 else word"""