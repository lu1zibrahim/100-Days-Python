def array_madness(a,b):
    sum1 = 0
    sum2 = 0
    for i in a:
        sum1 += i**2
    for i in b:
        sum2 += i**3
    return sum1 > sum2


#Better way
"""def array_madness(a,b):
    return sum(x ** 2 for x in a) > sum(x **3 for x in b)"""