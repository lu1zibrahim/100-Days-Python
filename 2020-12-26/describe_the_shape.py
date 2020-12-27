def describe_the_shape(angles):
    angle = int((angles-2)*180/angles)
    if angles <= 2:
        return "this will be a line segment or a dot"
    elif angles == 0:
        return 0
    else:
        return f"This shape has {angles} sides and each angle measures {angle}"


#Another way
"""def describe_the_shape(n):
    return  "this will be a line segment or a dot" if n < 3 else \
            "This shape has %s sides and each angle measures %s" % (n, (n-2)*180//n)"""