def hero(bullets, dragons):
    if bullets >= 2*dragons:
        return True
    else:
        return False

#Better way
#def hero(bullets, dragons):
#    return bullets >= dragons * 2