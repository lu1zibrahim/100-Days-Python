def next_id(arr):
    if not arr:
        return 0

    arr.sort()
    if arr[0] != 0:
        return 0

    for i in range(len(arr) - 1):
        if arr[i] - arr[i + 1] < -1:
            return arr[i] + 1

    return arr[-1] + 1


#Better way
#def next_id(arr):
#    t = 0
#    while t in arr:
#        t +=1
#    return t
