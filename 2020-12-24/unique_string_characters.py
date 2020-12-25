def solve(a,b):
    new_string = ""
    for item in a:
        if item not in b:
            new_string += item
    for item in b:
        if item not in a:
            new_string += item
    return new_string


#Another way
"""def solve(a,b):
    s = set(a)&set(b)
    return ''.join(c for c in a+b if c not in s)"""