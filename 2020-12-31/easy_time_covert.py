def time_convert(num):
    my_time = ""
    if num <= 0:
        return "00:00"
    else:
        return f"{num//60:02}:{num%60:02}"

#Another way
"""def timeConvert(m):
    return '{:02d}:{:02d}'.format(*divmod(max(int(m), 0), 60))"""