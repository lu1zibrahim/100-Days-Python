def isValid(formula):
    if 7 in formula or 8 in formula:
        if 1 in formula and 2 in formula:
            return False
        if 3 in formula and 4 in formula:
            return False
        if 5 in formula and 6 not in formula:
            return False
        if 6 in formula and 5 not in formula:
            return False
        else:
            return True
    else:
        return False

#A better python way
"""def isValid(formula):
  return not ( \
    (    1 in formula and     2 in formula) or \
    (    3 in formula and     4 in formula) or \
    (    5 in formula and not 6 in formula) or \
    (not 5 in formula and     6 in formula) or \
    (not 7 in formula and not 8 in formula))"""