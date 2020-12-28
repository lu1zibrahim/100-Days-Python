def alternateCase(s):
    new_string = ""
    for let in s:
        if let.islower():
            new_string += let.upper()
        else:
            new_string += let.lower()
    return new_string

#Another way
"""def alternateCase(s):
    return s.swapcase()"""