import unittest

from game import Game

from figures import King, Rook


# TODO: make more test case scenarios
class TestValidMoves(unittest.TestCase):
    def test_black_wins(self):
        game = Game('Ivan', 'George')
        game.move('d2', 'd4')
        game.move('c7', 'c6')
        game.move('a2', 'a4')
        game.move('d8', 'a5')
        self.assertEqual(game.move('a3', 'a5'), 'Player Black wins')

    def test_castling(self):
        game = Game('Gosho', 'Pesho')
        self.assertEqual(game.move('a1', 'e1'),
                         'Not a valid move, please try again!')
        game._board['b1'] = ''
        game._board['c1'] = ''
        game._board['d1'] = ''
        game.move('a1', 'e1')
        self.assertEqual(game._board['c1'], King('White'))
        self.assertEqual(game._board['d1'], Rook('White'))
        self.assertEqual(game._board['a1'], '')
        self.assertEqual(game._board['e1'], '')

if __name__ == '__main__':
    unittest.main()
