def index(array, n):
    try:
        return array[n]**n
    except IndexError:
        return -1


#Another way
# index(array, n):
#    return -1 if n >= len(array) else array[n] ** n