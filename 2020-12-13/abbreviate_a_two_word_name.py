def abbrev_name(name):
    return f"{name.split()[0][0].upper()}.{name.split()[1][0].upper()}"



#Another way
"""def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()"""
