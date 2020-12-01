def areYouPlayingBanjo(name):
    return f"{name} plays banjo" if name.split()[0][0].lower() == "r" else f"{name} does not play banjo"


#Another way
#def areYouPlayingBanjo(name):
#    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"