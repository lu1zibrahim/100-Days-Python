def ones_complement(binary_number):
    new_text = ""
    for let in binary_number:
        if let == "0":
            new_text += "1"
        else:
            new_text += "0"
    return new_text


#Another way
"""def ones_complement(n):
    return n.translate(str.maketrans("01","10"))"""