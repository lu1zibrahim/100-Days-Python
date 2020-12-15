def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages)-min(ages))


#Another creative way.
"""def difference_in_ages(ages):
    age = sorted(ages)
    return (age[0], age[-1], (age[-1]-age[0]))"""