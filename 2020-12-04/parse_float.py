def parse_float(string):
    my_lst = []
    try:
        for i in string.split():
            try:
                return float(i)
            except:
                return None
    except:
        try:
            return float(i)
        except:
            return None

#simpler way, way simpler
#def parse_float(string):
#    try:
#       return float(string)
#    except:
#        return None