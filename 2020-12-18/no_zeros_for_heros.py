def no_boring_zeros(n):
    if n == 0:
        return n
    else:
        while int(str(n)[-1]) == 0:
            n = int(str(n)[:-1])
        return n


#Another way, That function rstrip() is really something else
"""def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0"""