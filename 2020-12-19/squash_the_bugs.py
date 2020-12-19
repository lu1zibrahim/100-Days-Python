def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0
    while i < len(spl):
        if len(spl[i]) > longest:
            longest = len(spl[i])
            i += 1
        else:
            i += 1
    return longest

#This one is just to correct the bugs, but can be written in a better way
"""def find_longest(strng):
    return max(len(a) for a in strng.split())"""