import unittest

from game import Game


# TODO: make more test case scenarios
class TestValidMoves(unittest.TestCase):
    def test_black_wins(self):
        game = Game('Ivan', 'George')
        game.move('d2', 'd4')
        game.move('c7', 'c6')
        game.move('a2', 'a4')
        game.move('d8', 'a5')
        self.assertEqual(game.move('a3', 'a5'), 'Player Black wins')

if __name__ == '__main__':
    unittest.main()
