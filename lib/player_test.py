import unittest

from player import Player

from figures import LostFigures


class TestPlayer(unittest.TestCase):
    def test_to_string(self):
        player = Player('Ivan Georgiev')
        self.assertEqual(str(player), 'Player Ivan Georgiev')

if __name__ == '__main__':
    unittest.main()
