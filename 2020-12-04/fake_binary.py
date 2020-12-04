def fake_bin(x):
    fake = ""
    for i in x:
        if int(i) >= 5:
            fake = fake + "1"
        else:
            fake = fake + "0"
    return fake


#Better way
#def fake_bin(x):
#    return ''.join('0' if c < '5' else '1' for c in x)