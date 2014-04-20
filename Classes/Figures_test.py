import unittest

from Figures import Pawn, Knight, Bishop, Rook, Queen, King, LostFigures


class TestFigures(unittest.TestCase):
    def test_to_string(self):
        self.assertEqual(str(Pawn('White')), 'White Pawn')
        self.assertEqual(str(Knight('White')), 'White Knight')
        self.assertEqual(str(Bishop('White')), 'White Bishop')
        self.assertEqual(str(Rook('Black')), 'Black Rook')
        self.assertEqual(str(Queen('Black')), 'Black Queen')
        self.assertEqual(str(King('Black')), 'Black King')

    def test_symbols(self):
        self.assertEqual(Pawn('White')._symbol, '\033[37mP\033[0m')
        self.assertEqual(Knight('Black')._symbol, '\033[30mH\033[0m')

    def test_equals(self):
        self.assertEqual(Pawn('White'), Pawn('White'))
        self.assertNotEqual(Pawn('White'), Pawn('Black'))
        self.assertNotEqual(Pawn('White'), Knight('White'))


class TestLostFigures(unittest.TestCase):
    def setUp(self):
        self.lost_figures = LostFigures()
        self.lost_figures.add_figure(Pawn('White'))
        self.lost_figures.add_figure(Bishop('Black'))
        self.lost_figures_2 = LostFigures()
        self.lost_figures_2.add_figure(Pawn('White'))
        self.lost_figures_2.add_figure(Bishop('Black'))

    def test_add_and_index(self):
        self.assertEqual(self.lost_figures[0], Pawn('White'))
        self.assertEqual(self.lost_figures[1], Bishop('Black'))

    def test_equals(self):
        self.assertEqual(self.lost_figures, self.lost_figures_2)

    def test_to_string(self):
        self.assertEqual(str(self.lost_figures), ' White Pawn Black Bishop')

    def test_len(self):
        self.assertEqual(len(self.lost_figures), 2)

    def test_swap_pawn_for_figure(self):
        self.lost_figures.swap_pawn_for_figure(Bishop('Black'))
        self.assertEqual(self.lost_figures[-1], Pawn('Black'))

if __name__ == '__main__':
    unittest.main()
