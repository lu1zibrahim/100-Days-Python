def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False


#Another way
#def set_alarm(employed, vacation):
    #return employed and not vacation