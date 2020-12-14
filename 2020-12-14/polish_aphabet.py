alphabet = {
    "ą": "a",
    "ć": "c",
    "ę": "e",
    "ł": "l",
    "ń": "n",
    "ó": "o",
    "ś": "s",
    "ź": "z",
    "ż": "z"
}
def correct_polish_letters(st):
    translated = ""
    for i in st:
        if i in alphabet:
            translated += alphabet[i]
        else:
            translated += i
    return translated

#Better way
"""def correct_polish_letters(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))"""