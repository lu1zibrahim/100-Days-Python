def reverse_seq(n):
    i = 1
    lst = []
    while i <= n:
        lst.append(i)
        i += 1
    lst.sort(reverse=True)
    return lst

#Better way
#def reverseseq(n):
#    return list(range(n, 0, -1))