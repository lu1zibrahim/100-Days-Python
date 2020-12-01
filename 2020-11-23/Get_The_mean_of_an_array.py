import math
def get_average(marks):
    j = 0
    for i in marks:
        j = j + i
    return math.floor(j/len(marks))
    return j/len(marks)


#Another way
#def get_average(marks):
    #return sum(marks) // len(marks)