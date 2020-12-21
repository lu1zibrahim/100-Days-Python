def digitize(n):
    splt = str(n)
    lst = []
    for i in splt:
        lst.append(int(i))
    return lst[::-1]


#Better way
"""def digitize(n):
    return map(int, str(n)[::-1])"""