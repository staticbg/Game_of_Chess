import unittest

from multiplayer import MultiPlayer

from figures import King, Rook


class TestValidations(unittest.TestCase):
    def test_black_wins(self):
        game = MultiPlayer('Ivan', 'George')
        game.move('e2', 'e4')
        game.move('e7', 'e5')
        game.move('d1', 'h5')
        game.move('b8', 'c6')
        game.move('f1', 'c4')
        game.move('d7', 'd6')
        game.move('h5', 'f7')
        self.assertEqual(game.move('a3', 'a5'), 'Player Ivan wins')

    def test_castling(self):
        game = MultiPlayer('Gosho', 'Pesho')
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

    def test_resignation(self):
        game = MultiPlayer('Ivan', 'Pesho')
        self.assertEqual(game._resign(), 'Player Pesho wins')

        new_game = MultiPlayer('George', 'Kristian')
        new_game.move('a2', 'a4')
        self.assertEqual(new_game._resign(), 'Player George wins')

    def test_capture(self):
        game = MultiPlayer()
        game.move('b2', 'b4')
        game.move('a7', 'a5')
        game.move('b4', 'a5')

        self.assertEqual(game._player_black.show_lost_figures(), ' Black Pawn')

        game.move('a8', 'a5')
        game.move('b1', 'a3')
        game.move('a5', 'a3')

        self.assertEqual(game._player_white.show_lost_figures(),
                         ' White Pawn White Knight')

    def test_with_real_games(self):
        # http://www.chessgames.com/perl/chessgame?gid=1018910
        game = MultiPlayer('Adolf Anderssen',
                           'Lionel Adalbert Bagration Felix Kieseritsky')

        game.move('e2', 'e4')
        game.move('e7', 'e5')
        game.move('f2', 'f4')
        game.move('e5', 'f4')
        game.move('f1', 'c4')
        game.move('d8', 'h4')
        game.move('e1', 'f1')
        game.move('b7', 'b5')
        game.move('c4', 'b5')
        game.move('g8', 'f6')
        game.move('g1', 'f3')
        game.move('h4', 'h6')
        game.move('d2', 'd3')
        game.move('f6', 'h5')
        game.move('f3', 'h4')
        game.move('h6', 'g5')
        game.move('h4', 'f5')
        game.move('c7', 'c6')
        game.move('g2', 'g4')
        game.move('h5', 'f6')
        game.move('h1', 'g1')
        game.move('c6', 'b5')
        game.move('h2', 'h4')
        game.move('g5', 'g6')
        game.move('h4', 'h5')
        game.move('g6', 'g5')
        game.move('d1', 'f3')
        game.move('f6', 'g8')
        game.move('c1', 'f4')
        game.move('g5', 'f6')
        game.move('b1', 'c3')
        game.move('f8', 'c5')
        game.move('c3', 'd5')
        game.move('f6', 'b2')
        game.move('f4', 'd6')
        game.move('c5', 'g1')
        game.move('e4', 'e5')
        game.move('b2', 'a1')
        game.move('f1', 'e2')
        game.move('b8', 'a6')
        game.move('f5', 'g7')
        game.move('e8', 'd8')
        game.move('f3', 'f6')
        game.move('g8', 'f6')
        game.move('d6', 'e7')

        self.assertEqual(game.move('a3', 'a5'), 'Player Adolf Anderssen wins')
        self.assertEqual(game._player_black.show_lost_figures(),
                         ' Black Pawn Black Pawn Black Pawn')
        print(game._player_black.show_lost_figures())
        print(game._player_white.show_lost_figures())

        # http://www.chessgames.com/perl/chessgame?gid=1243022
        game = MultiPlayer('Gioachino Greco', 'NN')

        game.move('e2', 'e4')
        game.move('b7', 'b6')
        game.move('d2', 'd4')
        game.move('c8', 'b7')
        game.move('f1', 'd3')
        game.move('f7', 'f5')
        game.move('e4', 'f5')
        game.move('b7', 'g2')
        game.move('d1', 'h5')
        game.move('g7', 'g6')
        game.move('f5', 'g6')
        game.move('g8', 'f6')
        game.move('g6', 'h7')
        game.move('f6', 'h5')
        game.move('d3', 'g6')

        self.assertEqual(game.move('a3', 'a5'),
                         'Player Gioachino Greco wins')
        print(game._player_black.show_lost_figures())
        print(game._player_white.show_lost_figures())
        self.assertEqual(game._player_white.show_lost_figures(),
                         ' White Pawn White Queen')
        self.assertEqual(game._player_black.show_lost_figures(),
                         ' Black Pawn Black Pawn Black Pawn')

        # http://www.chessgames.com/perl/chessgame?gid=1339137
        game = MultiPlayer('Johan Upmark', 'Robin Johansson')

        game.move('c2', 'c4')
        game.move('h7', 'h5')
        game.move('h2', 'h4')
        game.move('a7', 'a5')
        game.move('d1', 'a4')
        game.move('a8', 'a6')
        game.move('a4', 'a5')
        game.move('a6', 'h6')
        game.move('a5', 'c7')
        game.move('f7', 'f6')
        game.move('c7', 'd7')
        game.move('e8', 'f7')
        game.move('d7', 'b7')
        game.move('d8', 'd3')
        game.move('b7', 'b8')
        game.move('d3', 'h7')
        game.move('b8', 'c8')
        game.move('f7', 'g6')
        game.move('c8', 'e6')

        self.assertEqual(game.move('a3', 'a5'),
                         '{}{}'.format('Player Johan Upmark and Player Robin ',
                                       'Johansson ended the game with a draw'))

# if __name__ == '__main__':
#    unittest.main()
