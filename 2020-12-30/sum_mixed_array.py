def sum_mix(arr):
    new_list = []
    for num in arr:
        if num == int:
            new_list.append(num)
        else:
            new_list.append(int(num))
    return sum(new_list)


#Another way
"""def sum_mix(arr):
    return sum(map(int, arr))"""