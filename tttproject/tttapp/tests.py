from django.test import TestCase, Client
from tttapp.gamelogic import TicTacToeBoard

class GameLogicTests(TestCase):
    def test_invalid_boards(self):
        for invalid_board in [
                '',
                (' ' * 10),
                'xxxxxxxxz',
        ]:
            self.assertFalse(TicTacToeBoard.is_valid(invalid_board))

    def test_valid_boards(self):
        for valid_board in [
                'x' + ' ' * 8,
                'xoxxoxxox',
        ]:
            self.assertTrue(TicTacToeBoard.is_valid(valid_board))


    #def test_find_o_winner(self):
    #a    board = TicTacToeBoard('ooo x x x')
    #    self.assertEqual(board.get_shallow_value(), 1)
