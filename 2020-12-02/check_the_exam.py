def check_exam(arr1,arr2):
    grade = 0
    i = 0
    while i <= 3:
        if arr1[i] == arr2[i]:
            grade = grade + 4
            i += 1
        elif arr2[i] == "":
            i += 1
        elif arr1[i] != arr2[i]:
            grade = grade -1
            i += 1
    return 0 if grade < 0 else grade


#def check_exam(arr1, arr2):
#    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))