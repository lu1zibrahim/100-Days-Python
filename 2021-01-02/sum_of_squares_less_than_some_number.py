import math
def get_number_of_squares(n):
    my_list = list(range(int(math.sqrt(n)+2)))
    squared_list = 0
    i = 0
    while squared_list <= n:
        squared_list += (my_list[i])**2
        if squared_list >= n:
            return my_list[i-1]
        else:
            i+=1


#Better way
"""def get_number_of_squares(n):
    s,i = 0,0
    while s < n:
        i += 1
        s += i**2
    return i-1"""