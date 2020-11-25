def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False


#Simpler Way
#def set_alarm(employed, vacation):
    #return employed and not vacation