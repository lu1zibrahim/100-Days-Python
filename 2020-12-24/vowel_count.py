vowels = ['a','e','i','o','u']
def get_count(input_str):
    num_vowels = 0
    for item in input_str:
        if item in vowels:
            num_vowels += 1
    return num_vowels


#Another way
"""def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")"""