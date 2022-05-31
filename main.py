import sys
from BoardPrinterProject.src.get_user_action import Action
from BoardPrinterProject.src.boards_manager import BoardsManager
from BoardPrinterProject.src.get_user_input import get_user_input


def main() -> None:

    loop = True
    while loop:
        output = get_user_input()
        if output[4]:
            loop = False
        else:
            print("Invalid input, please enter an integer.")
    running = True
    rows = output[0]
    columns = output[1]
    blank_char = output[2]
    board_name = output[3]

    b = BoardsManager()
    b.create_new_board(rows, columns, blank_char, board_name)
    b.generic_print()

    a = Action()
    action = a.get_user_action()

    while running:

        # fill spot
        if action == '1':
            new_char = str(input("Enter the character you want to add to the board: ").strip())
            new_pos = (input('Enter the position to place the character in the form row,col: ').strip())
            split = new_pos.split(",")
            new_row = int(split[0]) + 1
            new_column = int(split[1]) + 1
            b.place_new_char(new_row, new_column, new_char)
            b.generic_print()
            action = a.get_user_action()

        # erase spot
        elif action == '2':
            new_pos = input('Enter the position you want to erase in the form row, col: ').strip()
            split = new_pos.split(",")
            new_row = int(split[0]) + 1
            new_column = int(split[1]) + 1
            b.erase_old_char(new_row, new_column)
            b.generic_print()
            action = a.get_user_action()

        # switch board
        elif action == '3':
            for i, item in enumerate(b.list_of_boards_names):
                print(f"{i}. {item}")
            switch_index = int(input('Enter the number of the board you want to switch to: ').strip())
            b.switch_board(switch_index)
            b.generic_print()
            action = a.get_user_action()

        # create board
        elif action == '4':
            # automatically prints new board but is supposed to print 'active' board -> need to fix
            loop = True
            while loop:
                output = get_user_input()
                if output[4]:
                    loop = False
            rows = output[0]
            columns = output[1]
            blank_char = output[2]
            board_name = output[3]
            b.create_new_board(rows, columns, blank_char, board_name)
            b.generic_print()
            action = a.get_user_action()

        # quits the game
        elif action == '5':
            sys.exit()

        # shows input error
        else:
            print('Not valid action chosen')
            action = a.get_user_action()



if __name__ == '__main__':
    main()

