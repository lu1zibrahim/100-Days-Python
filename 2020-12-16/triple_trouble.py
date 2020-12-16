def triple_trouble(one, two, three):
    my_str = ""
    i = 0
    while i < len(one):
        my_str += one[i]+two[i]+three[i]
        i+= 1
    return my_str

#Another way
"""def triple_trouble(one, two, three):
    return ''.join(''.join(a) for a in zip(one, two, three))"""