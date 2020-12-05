def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer)) if limit % integer == 0 else list(range(integer, limit,integer))

#Simpler way
#def find_multiples(integer, limit):
#    return list(range(integer, limit+1, integer))