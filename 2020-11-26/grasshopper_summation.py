def summation(num):
    i = 1
    total = 0
    while i <= num:
        total = total + i
        i+=1
    return total

#Better way
#def summation(num):
#    return sum(range(1,num+1))