def even_chars(st):
    new_lst = []
    i = 0
    if len(st) <= 1 or len(st) > 100:
        return "invalid string"
    else:
        for item in st:
            if i % 2 != 0:
                new_lst += item
                i+=1
            else:
                i+=1
    return new_lst


#Another way
"""def even_chars(st):
    if len(st) < 2 or len(st)> 100:
        return 'invalid string'
    else:
        return [st[i] for i in range(1, len(st), 2)]"""