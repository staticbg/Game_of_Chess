import unittest

from figures import Pawn, Knight, Bishop, Rook, Queen, King

from board import Board


class TestFigures(unittest.TestCase):
    def test_to_string(self):
        self.assertEqual(str(Pawn('White')), 'White Pawn')
        self.assertEqual(str(Knight('White')), 'White Knight')
        self.assertEqual(str(Bishop('White')), 'White Bishop')
        self.assertEqual(str(Rook('Black')), 'Black Rook')
        self.assertEqual(str(Queen('Black')), 'Black Queen')
        self.assertEqual(str(King('Black')), 'Black King')

    def test_repr(self):
        self.assertEqual(repr(Pawn('White')), 'White Pawn')
        self.assertEqual(repr(Queen('Black')), 'Black Queen')

    def test_symbols(self):
        self.assertEqual(Pawn('White')._symbol, '\033[37mP\033[0m')
        self.assertEqual(Knight('Black')._symbol, '\033[30mH\033[0m')

    def test_equals(self):
        self.assertEqual(Pawn('White'), Pawn('White'))
        self.assertNotEqual(Pawn('White'), Pawn('Black'))
        self.assertNotEqual(Pawn('White'), Knight('White'))

# if __name__ == '__main__':
#    unittest.main()
