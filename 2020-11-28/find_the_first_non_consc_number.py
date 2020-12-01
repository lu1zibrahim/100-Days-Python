def first_non_consecutive(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]-1:
            i+=1
        else:
            return arr[i+1]
    return None



#Better way
#def first_non_consecutive(arr):
#    if not arr: return 0
#    for i, x in enumerate(arr[:-1]):
#        if x + 1 != arr[i + 1]:
#           return arr[i + 1]
