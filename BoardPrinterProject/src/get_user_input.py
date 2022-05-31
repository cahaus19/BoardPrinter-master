from typing import Tuple

def get_user_input() -> Tuple[int, int, str, str, bool]:
    board_name =  input('Enter the name of your board: ').strip()
    str_rows =  input('Enter the number of rows for your board: ').strip()
    str_col = input('Enter the number of columns for your board: ').strip()
    blank_char = input('Enter the blank character to be used on your board: ').strip()
    rows = 0
    columns = 0
    if str_rows.isnumeric():
        good_flag_row = True
        rows = int(str_rows)
    else:
        good_flag_row = False
    if str_col.isnumeric():
        good_flag_col = True
        columns = int(str_col)
    else:
        good_flag_col = False

    if good_flag_row and good_flag_col:
        good_flag = True
    else:
        good_flag = False

    return rows, columns, blank_char, board_name, good_flag

