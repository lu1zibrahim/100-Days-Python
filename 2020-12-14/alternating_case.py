def to_alternating_case(string):
    alternating = ""
    for i in string:
        if i.islower():
            alternating += i.upper()
        elif i.isupper():
            alternating += i.lower()
        else:
            alternating += i
    return alternating


#Another way, well I learned the islower() and isupper(), but the swapcase() really surprised me.
#Python is a wonderful language
"""def to_alternating_case(string):
    return string.swapcase()"""