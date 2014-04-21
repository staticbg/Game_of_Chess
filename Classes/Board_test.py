import unittest

from Figures import Pawn, Knight, Bishop, Rook, Queen, King

from Board import Board


class TestBoard(unittest.TestCase):
    def test_get_item(self):
        board = Board()
        self.assertEqual(board['A8'], Rook('Black'))
        self.assertEqual(board['G8'], Knight('Black'))
        self.assertEqual(board['C1'], Bishop('White'))
        self.assertEqual(board['e2'], Pawn('White'))
        self.assertEqual(board['f5'], '')

    def test_to_string(self):
        board = Board()
        self.assertEqual(str(board), '8 |\033[30mR\033[0m|\033[30mH\033[0m|'
                                     '\033[30mB\033[0m|\033[30mQ\033[0m|'
                                     '\033[30mK\033[0m|\033[30mB\033[0m|'
                                     '\033[30mH\033[0m|\033[30mR\033[0m|\n'
                                     '7 |\033[30mP\033[0m|\033[30mP\033[0m|'
                                     '\033[30mP\033[0m|\033[30mP\033[0m|'
                                     '\033[30mP\033[0m|\033[30mP\033[0m|'
                                     '\033[30mP\033[0m|\033[30mP\033[0m|\n'
                                     '6 | | | | | | | | |\n'
                                     '5 | | | | | | | | |\n'
                                     '4 | | | | | | | | |\n'
                                     '3 | | | | | | | | |\n'
                                     '2 |\033[37mP\033[0m|\033[37mP\033[0m|'
                                     '\033[37mP\033[0m|\033[37mP\033[0m|'
                                     '\033[37mP\033[0m|\033[37mP\033[0m|'
                                     '\033[37mP\033[0m|\033[37mP\033[0m|\n'
                                     '1 |\033[37mR\033[0m|\033[37mH\033[0m|'
                                     '\033[37mB\033[0m|\033[37mQ\033[0m|'
                                     '\033[37mK\033[0m|\033[37mB\033[0m|'
                                     '\033[37mH\033[0m|\033[37mR\033[0m|\n'
                                     '   A B C D E F G H')

if __name__ == '__main__':
    unittest.main()
