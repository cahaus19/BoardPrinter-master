import unittest
from unittest.mock import patch
from BoardPrinterProject.src.boards_manager import BoardsManager


class TestBoardsManager(unittest.TestCase):

    def test_create_board(self):
        self.rows = 2
        self. columns = 2
        self.blank_char = '.'
        self.board_name = 'tic tac toe'
        self.list_of_boards = []
        self.list_of_boards_names = []
        user_input = (2, 2, '.', 'tic tac toe')
        with patch('BoardPrinterProject.src.boards_manager.input', side_effects = user_input):
            test_name = ['tic tac toe']
            self.assertListEqual(test_name, BoardsManager.create_new_board(self, 2, 2, '.', 'tic tac toe'))

    def test_switch_board(self):
        self.active_board_index = 0
        self.switch_board = 1
        user_input = 1
        with patch('BoardPrinterProject.src.boards_manager.input', side_effects=user_input):
            ans = 1
            self.assertEqual(1, BoardsManager.switch_board(self, 1))

    def test_kill_program(self):
        self.game_status = False
        self.assertFalse(self.game_status)

    def test_generic_print(self):
        self.active_board_index = 0
        self.list_of_boards = [[[' ',0, 1], [0, '.', '.'], [1, '.', '.']]]
        self.assertListEqual([[' ', 0, 1], [0, '.', '.'], [1, '.', '.']], BoardsManager.generic_print(self))


if __name__ == '__main__':
    unittest.main()
