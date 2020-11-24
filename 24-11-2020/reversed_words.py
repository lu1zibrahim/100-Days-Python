def reverseWords(s):
    r = s.split()
    t = " ".join(r[::-1])
    return t

#Better way
#def reverseWords(str):
    #return " ".join(str.split(" ")[::-1])