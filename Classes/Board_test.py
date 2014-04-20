import unittest

from Figures import Pawn, Knight, Bishop, Rook, Queen, King

from Board import Board


class TestBoard(unittest.TestCase):
    def test_get_item(self):
        board = Board()
        self.assertEqual(board[0], [Rook('Black'), Knight('Black'),
                                    Bishop('Black'), Queen('Black'),
                                    King('Black'), Bishop('Black'),
                                    Knight('Black'), Rook('Black')])
        self.assertEqual(board[7], [Rook('White'), Knight('White'),
                                    Bishop('White'), Queen('White'),
                                    King('White'), Bishop('White'),
                                    Knight('White'), Rook('White')])
        for row in range(2, 6):
            self.assertEqual(board[row], ['']*8)

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
