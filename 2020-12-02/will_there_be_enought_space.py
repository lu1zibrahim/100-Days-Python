def enough(cap, on, wait):
    return 0 if cap>= on+wait else on+wait-cap


#Another way
#def enough(cap, on, wait):
#    return max(0, wait - (cap - on))
