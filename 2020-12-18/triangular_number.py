def is_triangular(t):
    sum = 0
    n = 1
    while(sum <= t):
        sum += n
        if (sum == t):
            return True
        n += 1
    return False


#Another way
"""def is_triangular(t):
    x = int((t*2)**0.5)
    return t == x*(x+1)/2"""