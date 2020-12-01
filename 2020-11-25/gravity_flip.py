def flip(d, a):
    if d == 'R':
        a.sort()
        return a
    elif d == 'L':
        a.sort(reverse=True)
        return a


#Another way
#def flip(d,a):
    #return sorted(a, reverse=d=='L')