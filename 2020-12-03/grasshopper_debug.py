def weather_info(temp):
    c = convert_to_celsius(temp)
    if (c < 0):
        return f"{c} is freezing temperature"
    else:
        return f"{c} is above freezing temperature"


def convert_to_celsius(temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius


#Another way, but this was not debug, but a new code
#def weather_info (t):
#  c = (t - 32) * (5.0 /9)
#  return str(c) + " is freezing temperature" if c <= 0 else str(c) + " is above freezing temperature"