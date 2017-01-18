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
        self.assertEqual(gamelogic.get_shallow_value('o   o   o'), 1)
        self.assertEqual(gamelogic.get_shallow_value('x   x   x'), 0)
        self.assertEqual(gamelogic.get_shallow_value('         '), None)

    def test_generate_move_options(self):
        self.assertEqual(gamelogic.get_next_board_options('         ', 'o'), [
            'o        ',
            ' o       ',
            '  o      ',
            '   o     ',
            '    o    ',
            '     o   ',
            '      o  ',
            '       o ',
            '        o',
        ])

    def test_is_playable(self):
        self.assertTrue(gamelogic.is_playable_by_o('         '))
        self.assertFalse(gamelogic.is_playable_by_o('o        '))
        self.assertTrue(gamelogic.is_playable_by_o('x        '))
        self.assertFalse(gamelogic.is_playable_by_o('xx       '))

    def test_minimax(self):
        self.assertEqual(gamelogic.minimax_value('ooo      ', True), 1)
        #self.assertEqual(gamelogic.minimax_value('oo       '), 1)
