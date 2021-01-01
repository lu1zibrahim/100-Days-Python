def filter_long_words(sentence, n):
    my_lst = []
    for word in sentence.split():
        if len(word) > n:
            my_lst.append(word)
    return my_lst


#Another way
"""def filter_long_words(sentence,long):
    return [word for word in sentence.split() if len(word) > long]"""