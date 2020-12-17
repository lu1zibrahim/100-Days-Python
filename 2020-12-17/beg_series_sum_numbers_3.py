def get_sum(a,b):
    if a == b:
        return a
    elif a < b:
        my_list=range(a,b+1)
        return sum(my_list)
    elif b < a:
        my_list=range(b,a+1)
        return sum(my_list)

#Better way
"""def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))"""