def red_knight(N, P):
    color = ""
    if (P - N) % 2 == 0:
        color = "White"
    else:
        color = "Black"
    return (color,2*P)

#def red_knight(N, P):
"""    return ('White' if P % 2 == N else 'Black', P * 2) """