# mine first solution

def multi_table(number):
    n = 1
    my_list = []
    final = ""
    while n <= 10:
        result = n*number
        multi = f"{n} * {number} = {result}"
        n = n + 1
        my_list.append(multi)
    final = "\n".join(my_list)
    return final



# Cleaner one
#def multi_table(number):
    #return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))