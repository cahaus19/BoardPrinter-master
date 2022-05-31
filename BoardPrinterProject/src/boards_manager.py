# place your BoardsManager class in this file
from BoardPrinterProject.src.board import Board
from typing import Iterable, List, TypeVar, Any
T = TypeVar('T')



class BoardsManager(object):

    def __init__(self) -> None:
        self.game_status = True
        self.active_board_index = -1
        self.list_of_boards = [] #type: ignore 
        self.list_of_boards_names = [] #type: ignore

    def create_new_board(self, rows: int, columns: int, blank_char: str, board_name: str) -> None:
        my_board = Board(rows, columns, blank_char, board_name)
        self.list_of_boards.insert(0, my_board)
        self.list_of_boards_names.insert(0, board_name)
        self.active_board_index += 1

    def switch_board(self, switch_board: int) -> None:
        self.active_board_index = switch_board

    def place_new_char(self, new_row: int, new_column: int, new_char: str) -> None:
        boardy_boi = self.list_of_boards[self.active_board_index]
        boardy_boi.add_new_char(new_row, new_column, new_char)
        self.list_of_boards[self.active_board_index] = boardy_boi

    def erase_old_char(self, new_row: int, new_column: int) -> None:
        boardy_boi = self.list_of_boards[self.active_board_index]
        boardy_boi.erase_char(new_row, new_column)
        self.list_of_boards[self.active_board_index] = boardy_boi

    def kill_program(self) -> bool:
        self.game_status = False
        return self.game_status

    def generic_print(self) -> None:
        boardy_boi = self.list_of_boards[self.active_board_index]
        print(boardy_boi)














