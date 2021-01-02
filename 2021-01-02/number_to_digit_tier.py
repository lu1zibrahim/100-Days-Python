def create_array_of_tiers(n):
    my_list = []
    i = 0
    while i < len(str(n)):
        my_list.append(str(n)[:(i+1)])
        i += 1
    return my_list



#Another way
"""def create_array_of_tiers(n):
    n=str(n)
    return [n[:i] for i in range(1,len(n)+1)]"""