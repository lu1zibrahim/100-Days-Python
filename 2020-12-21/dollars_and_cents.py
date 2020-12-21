def format_money(amount):
    return "${:0,.2f}".format(amount).replace('$-','-$')


#Another way
"""def format_money(amount):
    return '${:.2f}'.format(amount)"""