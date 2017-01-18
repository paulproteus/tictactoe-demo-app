from django.test import TestCase, Client
from tttapp import gamelogic

class GameLogicTests(TestCase):
    def test_invalid_boards(self):
        for invalid_board in [
                '',
                (' ' * 10),
                'xxxxxxxxz',
        ]:
            self.assertFalse(gamelogic.board_is_valid(invalid_board))

    def test_valid_boards(self):
        for valid_board in [
                'x' + ' ' * 8,
                'xoxxoxxox',
        ]:
            self.assertTrue(gamelogic.board_is_valid(valid_board))


    def test_find_winners(self):
        self.assertEqual(gamelogic.get_shallow_value('ooo      '), 1)
        self.assertEqual(gamelogic.get_shallow_value('xxx      '), 0)
        self.assertEqual(gamelogic.get_shallow_value('o  o  o  '), 1)
        self.assertEqual(gamelogic.get_shallow_value(' x  x  x '), 0)
