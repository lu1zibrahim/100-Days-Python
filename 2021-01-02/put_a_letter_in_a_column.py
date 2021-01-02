import re
def build_row_text(index, character):
    board = "| | | | | | | | | |"
    board_final = re.split('(\W)',board)
    board_final[(4*(index+1))-1] = character
    return ("".join(board_final))

#Another and better way
"""    a=list('|||||||||')
    a[index]="|"+character+"|"
    return " ".join(a)"""