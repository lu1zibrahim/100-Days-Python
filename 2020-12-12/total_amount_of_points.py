def points(games):
    totalpoints = 0
    for i in games:
        if int(i[0]) > int(i[2]):
            totalpoints += 3
        elif int(i[0]) < int(i[2]):
            totalpoints += 0
        else:
            totalpoints += 1
    return totalpoints

#Better way
"""def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count"""