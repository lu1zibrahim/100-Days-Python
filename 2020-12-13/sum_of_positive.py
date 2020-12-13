def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum


#Better way
"""def positive_sum(arr):
    return sum(x for x in arr if x > 0)"""