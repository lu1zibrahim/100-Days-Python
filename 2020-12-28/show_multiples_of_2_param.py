# Python version: return multiples of 2 numbers in a list
def multiples(s1,s2,s3):
    my_list = []
    for num in list(range(s1,s3)):
        if num % s1 == 0 and num % s2 == 0:
            my_list.append(num)
    return my_list


#A more python way
"""# Pyton version: return multiples of 2 numbers in a list
def multiples(s1,s2,s3):
    return [x for x in range(s1, s3) if x % s1 == 0 and x % s2 == 0]"""