
def burner(c,h,o):
    water = 0
    co2 = 0
    methane = 0
    carbon = c
    hidrogen = h
    oxigen = o
    if hidrogen >= 2 and oxigen > 0:
        if 2*oxigen < hidrogen:
            waterO = oxigen
            waterH = waterO
            oxigen -=waterO
            hidrogen -= 2*waterH
            water = waterH
        else:
            waterH = h // 2
            waterO = waterH
            oxigen -= waterO
            hidrogen -= 2*waterH
            water = waterH
    if carbon > 0 and oxigen >= 2:
        if 2*carbon < oxigen:
            co2O = carbon
            co2C = co2O
            oxigen -= 2*co2O
            carbon -=co2C
            co2 = co2O
        else:
            co2O = oxigen//2
            co2C = co2O
            oxigen -= 2*co2O
            carbon -= co2C
            co2 = co2O
    if hidrogen >= 4 and carbon > 0:
        if 4*carbon < hidrogen:
            ch4C = carbon
            ch4H = carbon
            hidrogen -= 4*carbon
            carbon -= carbon
            methane = ch4C
        else:
            ch4H = hidrogen//4
            ch4C = ch4H
            hidrogen -=4*ch4H
            carbon -= ch4H
            methane = ch4H
    return water,co2,methane


#Well, my solution was crap, but it works, but is was crap
"""def burner(c,h,o):
    water = co2 = methane = 0
    
    while h > 1 and o > 0:
        water += 1
        h -= 2
        o -= 1
    
    while c > 0 and o > 1:
        co2 += 1
        c -= 1
        o -= 2
        
    while c > 0 and h > 3:
        methane += 1
        c -= 1
        h -= 4
        
    return water,co2,methane"""