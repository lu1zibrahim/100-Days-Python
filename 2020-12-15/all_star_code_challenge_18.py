def str_count(strng, letter):
    counter = 0
    for i in strng:
        if letter in i:
            counter +=1
    return counter

#Better way
"""def strCount(string, letter):
    return string.count(letter)"""