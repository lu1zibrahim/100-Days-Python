def invert(lst):
    inverted_list = []
    for i in lst:
        inverted_list.append(-i)
    return inverted_list

#Another way
#def invert(lst):
#    return [-x for x in lst]

#Another way
#def invert(lst):
#    return list(map(lambda x: -x, lst));