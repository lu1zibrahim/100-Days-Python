def cooking_time(eggs):
    if eggs == 0:
        return 0
    elif eggs % 8 == 0:
        return eggs//8 * 5
    else:
        return (eggs//8+1)*5


#Another way
"""from math import *

def cooking_time(eggs):
    return 5*ceil(eggs/8.0)"""