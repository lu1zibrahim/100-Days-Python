def find_it(seq):
    number = 0
    for num in seq:
        if seq.count(num) % 2 != 0:
            number = num
    return number

#Another wat
"""def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i"""