def cube_sum(n, m):
    sum = 0
    if n == m:
        return 0
    elif n > m:
        for item in range(m+1,n+1):
            sum += item**3
    else:
        for item in range(n+1,m+1):
            sum += item**3
    return sum


#Another way
"""def cube_sum(n, m):
    n, m = sorted([n, m])
    return sum(i ** 3 for i in range(n + 1, m + 1))"""