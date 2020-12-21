def get_real_floor(n):
    if n == 1 or n ==0:
        return 0
    elif n >= 13:
        return n-2
    elif n < 0:
        return n
    else:
        return n-1


#Another way
"""def get_real_floor(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2"""