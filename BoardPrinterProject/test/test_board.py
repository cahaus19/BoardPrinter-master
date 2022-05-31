import unittest
from unittest.mock import patch
from BoardPrinterProject.src.board import Board
from BoardPrinterProject.src.get_user_action import Action

class TestBoard(unittest.TestCase):


    def test_create_board(self):
        user_input = (2, 2, '.')
        self.rows = 2
        self.columns = 2
        self.blank_char = '.'
        with patch('BoardPrinterProject.src.board.input', side_effect = user_input):
            self.assertEqual([[' ',0, 1], [0, '.', '.'], [1, '.', '.']], Board.create_board(self))

    def test_add_new_char(self):
        user_input = (1, 1, '#')
        self.board_gen = [[' ',0, 1], [0, '.', '.'], [1, '.', '.']]
        self.new_char = 'X'
        self.blank_char = '.'
        self.board_gen[1][1] = self.blank_char

        with patch('BoardPrinterProject.src.input', side_effect = user_input):
            self.assertEqual([[' ',0, 1], [0, 'X', '.'], [1, '.', '.']], Board.add_new_char(self, 1,  1, 'X'))

    def test_erase_char(self):
        user_input = (1, 1)
        self.blank_char = '.'
        self.board_gen = [[' ',0, 1], [0, 'X', '.'], [1, '.', '.']]

        with patch('BoardPrinterProject.src.input', side_effect=user_input):
            self.assertEqual([[' ', 0, 1], [0, '.', '.'], [1, '.', '.']], Board.erase_char(self, 1, 1))


if __name__ == '__main__':
    unittest.main()
