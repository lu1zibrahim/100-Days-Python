import math

def next_perfect_square(n):
    if n < 0:
        return 0
    else:
        return int(math.sqrt(n) + 1) ** 2

#Another way
"""def next_perfect_square(n):
    return n>=0 and (int(n**0.5)+1)**2"""