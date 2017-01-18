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
        # The empty board is playable.
        self.assertTrue(gamelogic.is_playable_by_o('         '))
        # A board with one 'o is not playable -- it would mean 'o'
        # goes twice in a row.
        self.assertFalse(gamelogic.is_playable_by_o('o        '))
        # A board with one 'x' is playable. It means 'o' went second.
        self.assertTrue(gamelogic.is_playable_by_o('x        '))
        # A board with two 'x's is not playable. It means 'o' got
        # their turn skipped.
        self.assertFalse(gamelogic.is_playable_by_o('xx       '))

    def test_minimax(self):
        # This board is winnable by the base case.
        self.assertEqual(gamelogic.minimax_value('ooo      ', 'o'), 1)
        # This board is winnable by making one move.
        self.assertEqual(gamelogic.minimax_value('oo       ', 'o'), 1)
        # This board is winnable (by x) by making one move.
        self.assertEqual(gamelogic.minimax_value('xx       ', 'x'), 0)
        # The empty board can be won, in theory.
        self.assertEqual(gamelogic.minimax_value('         ', 'o'), 1)

    def test_get_best_move(self):
        # This test comes from the specification.
        self.assertEqual(gamelogic.get_best_move(' xxo  o  '),
                         'oxxo  o  ')
        # This test relies on an implementation detail, which is the
        # fact that we always play in the top-left corner, i.e. the
        # first way we can find that would lead to a victory.
        self.assertEqual(gamelogic.get_best_move('         '),
                         'o        ')
        # Test that we stop x from winning on the bottom row.
        self.assertEqual(gamelogic.get_best_move(' o     xx'),
                         ' o    oxx')
        # Test that we successfully allow ourselves to win.
        self.assertEqual(gamelogic.get_best_move('x   x  oo '),
                         'x   x  ooo')
