def remove_every_other(my_list):
    lst = []
    i = 0
    while i < len(my_list):
        for j in my_list:
            if i % 2 == 0:
                lst.append(j)
                i += 1
            else:
                i += 1
    return lst

#Better way, THis was really sad
"""def remove_every_other(my_list):
    return my_list[::2]"""