def get_missing_element(seq):
    lst = list(range(0,10))
    item = 0
    for num in seq:
        if num in lst:
            lst.remove(num)
    return lst[0]


#Another way
"""def get_missing_element(seq): 
    return 45 - sum(seq)"""