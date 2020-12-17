def get_grade(s1, s2, s3):
    sum = (s1+s2+s3)/3
    if sum >= 90:
        return "A"
    elif sum >= 80:
        return "B"
    elif sum >= 70:
        return "C"
    elif sum >= 60:
        return "D"
    else:
        return "F"