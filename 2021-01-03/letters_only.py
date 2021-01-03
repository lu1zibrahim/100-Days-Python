alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def remove_chars(s):
    new_string = ""
    for let in s:
        if let.lower() in alphabet or let == " ":
            new_string += let
    return new_string

#Another way
"""import re

def remove_chars(s):
    return re.sub(r'[^a-zA-Z ]', '', s)"""