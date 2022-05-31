# Place your Board class in this file
from typing import List, TypeVar
T = TypeVar('T')


class Board(object):

    def __init__(self, rows: int, columns: int, blank_char: str, board_name: str) -> None: #type: ignore
        self.rows = rows
        self.columns = columns
        self.blank_char = blank_char
        self.board_name = board_name
        self.board_gen = []
        self.create_board()  #type: ignore
        self.new_char = None

    def create_board(self) -> List[str]:
        int_row = int(self.rows)
        int_col = int(self.columns)
        n = int_row + 1
        m = int_col + 1
        self.board_gen = ([[i + j for j in range(m)] for i in range(n)])
        for i in range(len(self.board_gen)):
            for j in range(len(self.board_gen[i])): # type: ignore
                if i * j != 0:
                    self.board_gen[i][j] = self.blank_char # type: ignore
                else:
                    if self.board_gen[i][j] == 0:
                        self.board_gen[i][j] = ' '  # type: ignore
                    else:
                        self.board_gen[i][j] = self.board_gen[i][j]-1
        return self.board_gen

    def add_new_char(self, new_row: int, new_column: int, new_char: str) -> str:
        self.new_char = new_char
        self.board_gen[new_row][new_column] = new_char


    def erase_char(self,  new_row: int, new_column:int) -> None:
        self.board_gen[new_row][new_column] = self.blank_char


    def __str__(self) -> str:
        stringy_boi = str(self.board_name) + '\n'
        for i in range(len(self.board_gen)):
            for j in range(len(self.board_gen[i])):
                if j + 1 < len(self.board_gen[i]):
                    stringy_boi += str(self.board_gen[i][j]) + ' '
                elif j + 1 <= len(self.board_gen[i]):
                    stringy_boi += str(self.board_gen[i][j])
            if i + 1 < len(self.board_gen):
                stringy_boi += '\n'
        return stringy_boi




