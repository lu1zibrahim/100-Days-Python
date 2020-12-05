def solution(a, b):
    lst = ""
    if len(a) < len(b):
        lst = lst + a
        lst = lst + b
        lst = lst + a
        return lst
    else:
        lst = lst + b
        lst = lst + a
        lst = lst + b
        return lst


#Better way
#def solution(a, b):
#    return a+b+a if len(a)<len(b) else b+a+b