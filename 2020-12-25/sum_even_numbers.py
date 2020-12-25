def sum_even_numbers(seq):
    even = 0
    for item in seq:
        if item % 2 ==0:
            even += item
    return even

#Another way
"""def sum_even_numbers(seq): 
    return sum(n for n in seq if not n % 2)"""