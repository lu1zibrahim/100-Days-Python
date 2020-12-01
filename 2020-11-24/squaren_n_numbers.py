def square_sum(numbers):
    total = 0
    for i in numbers:
        j = i*i
        total = total + j
    return total


#Another and more like python way
#def square_sum(numbers):
    #return sum(x ** 2 for x in numbers)