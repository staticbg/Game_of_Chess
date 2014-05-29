import unittest

from player import Player

from figures import LostFigures, Pawn, Rook


class TestPlayer(unittest.TestCase):
    def test_to_string(self):
        player = Player('Ivan Georgiev')
        self.assertEqual(str(player), 'Player Ivan Georgiev')

    def test_add_to_lost_figures(self):
        player = Player('s')

        player.add_figure(Pawn('White'))
        player.add_figure(Rook('White'))
        self.assertEqual(player._lost_figures[0], Pawn('White'))
        self.assertEqual(player._lost_figures[1], Rook('White'))

        self.assertEqual(player.show_lost_figures(), ' White Pawn White Rook')

if __name__ == '__main__':
    unittest.main()
