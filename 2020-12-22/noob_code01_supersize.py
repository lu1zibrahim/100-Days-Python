def super_size(n):
    lst = []
    for i in str(n):
        lst.append(int(i))
    splt = sorted(lst, reverse=True)
    my_str = ""
    for j in splt:
        my_str += str(j)
    return int(my_str)


#More python way
"""def super_size(n):
    return int(''.join(sorted(str(n), reverse = True)))"""