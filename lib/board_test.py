import unittest

from figures import Pawn, Knight, Bishop, Rook, Queen, King

from constants import ALL_BOARD_POSITIONS

from board import Board


class TestValidations(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        for index in range(ord('A'), ord('H') + 1):
            position = '{}2'.format(chr(index))
            self.board[position] = ''

    def test_pawn_move(self):
        self.assertTrue(self.board['a7']
                        ._pawn_valid_move(self.board, 'A7', 'A6'))
        self.assertFalse(self.board['c7']
                         ._pawn_valid_move(self.board, 'c7', 'd5'))
        self.assertFalse(self.board['c7']
                         ._pawn_valid_move(self.board, 'cd7', 'csd5'))
        self.board['d6'] = Queen('White')
        self.assertTrue(self.board['e7']
                        ._pawn_valid_move(self.board, 'e7', 'd6'))
        self.board['d6'] = ''

        self.board['c5'] = Pawn('White')
        self.board['c6'] = Rook('White')
        self.board['d6'] = Queen('White')
        self.board['h5'] = Pawn('White')
        self.board['d3'] = Pawn('White')
        self.board['c4'] = Rook('Black')
        self.board['d4'] = Queen('Black')
        self.board['e4'] = Bishop('Black')

        self.assertTrue(self.board['d3']
                        ._pawn_valid_move(self.board, 'd3', 'c4'))
        self.assertTrue(self.board['d3']
                        ._pawn_valid_move(self.board, 'd3', 'e4'))
        self.assertFalse(self.board['d3']
                         ._pawn_valid_move(self.board, 'd3', 'd4'))
        self.assertFalse(self.board['c5']
                         ._pawn_valid_move(self.board, 'c5', 'b6'))
        self.assertFalse(self.board['c5']
                         ._pawn_valid_move(self.board, 'c5', 'c6'))
        self.assertFalse(self.board['c5']
                         ._pawn_valid_move(self.board, 'c5', 'd6'))
        self.assertTrue(self.board['h5']
                        ._pawn_valid_move(self.board, 'h5', 'h6'))
        self.assertFalse(self.board['h5']
                         ._pawn_valid_move(self.board, 'h5', 'h4'))
        self.assertFalse(self.board['h5']
                         ._pawn_valid_move(self.board, 'h5', 'g4'))
        self.assertFalse(self.board['h5']
                         ._pawn_valid_move(self.board, 'h5', 'a5'))

        self.board['c6'] = ''
        self.board['d7'] = ''
        self.board['h5'] = ''
        self.board['d3'] = ''
        self.board['c4'] = ''
        self.board['d4'] = ''
        self.board['e4'] = ''
        self.board['c5'] = ''

        self.assertTrue(self.board['c7']
                        ._pawn_valid_move(self.board, 'c7', 'c5'))
        self.board['c7'] = ''

        self.board['a2'] = Pawn('White')
        self.assertTrue(self.board['a2']
                        ._pawn_valid_move(self.board, 'a2', 'a4'))
        self.board['a3'] = Rook('White')
        self.assertFalse(self.board['a2']
                         ._pawn_valid_move(self.board, 'a2', 'a4'))
        self.board['a3'] = ''
        self.board['a4'] = Pawn('Black')
        self.assertFalse(self.board['a2']
                         ._pawn_valid_move(self.board, 'a2', 'a4'))
        self.board['a4'] = Pawn('White')
        self.assertFalse(self.board['a2']
                         ._pawn_valid_move(self.board, 'a2', 'a4'))

        self.board['a4'] = ''
        self.board['a2']._moved = True
        self.assertFalse(self.board['a2']
                         ._pawn_valid_move(self.board, 'a2', 'a4'))
        self.board['a2'] = ''

        self.board['a4'] = Pawn('White')
        self.assertFalse(self.board['a4']
                         ._pawn_valid_move(self.board, 'a4', 'a6'))
        self.board['a4'] = ''

    def test_rook_move(self):
        self.assertTrue(self.board['a1']
                        ._rook_valid_move(self.board, 'A1', 'a5'))
        self.assertTrue(self.board['a1']
                        ._rook_valid_move(self.board, 'A1', 'a6'))
        self.assertTrue(self.board['a1']
                        ._rook_valid_move(self.board, 'A1', 'a7'))
        self.board['a3'] = King('White')
        self.assertFalse(self.board['a1']
                         ._rook_valid_move(self.board, 'A1', 'a3'))
        self.assertFalse(self.board['a1']
                         ._rook_valid_move(self.board, 'A1', 'a5'))
        self.board['a2'] = Rook('White')
        self.assertTrue(self.board['a2']
                        ._rook_valid_move(self.board, 'A2', 'e2'))
        self.assertFalse(self.board['a2']
                         ._rook_valid_move(self.board, 'A2', 'c4'))
        self.board['a3'] = ''
        self.board['a2'] = ''

        self.board['c3'] = Rook('Black')
        self.board['c7'] = Pawn('Black')
        self.board['d4'] = Bishop('White')
        self.board['e3'] = Pawn('White')

        self.assertTrue(self.board['c3']
                        ._rook_valid_move(self.board, 'c3', 'b3'))
        self.assertTrue(self.board['c3']
                        ._rook_valid_move(self.board, 'c3', 'c4'))
        self.assertTrue(self.board['c3']
                        ._rook_valid_move(self.board, 'c3', 'c2'))
        self.assertTrue(self.board['c3']
                        ._rook_valid_move(self.board, 'c3', 'c6'))
        self.assertFalse(self.board['c3']
                         ._rook_valid_move(self.board, 'c3', 'c7'))
        self.assertFalse(self.board['c3']
                         ._rook_valid_move(self.board, 'c3', 'c8'))
        self.assertTrue(self.board['c3']
                        ._rook_valid_move(self.board, 'c3', 'a3'))
        self.assertTrue(self.board['c3']
                        ._rook_valid_move(self.board, 'c3', 'e3'))
        self.assertFalse(self.board['c3']
                         ._rook_valid_move(self.board, 'c3', 'f3'))
        self.assertFalse(self.board['c3']
                         ._rook_valid_move(self.board, 'c3', 'e5'))
        self.assertFalse(self.board['c3']
                         ._rook_valid_move(self.board, 'c3', 'b2'))
        self.assertFalse(self.board['c3']
                         ._rook_valid_move(self.board, 'c3', 'e9'))

        self.board['c3'] = ''
        self.board['c7'] = ''
        self.board['d4'] = ''
        self.board['e3'] = ''

    def test_knight_move(self):
        self.board['c4'] = Knight('White')
        self.board['b2'] = Queen('White')
        self.board['e5'] = Pawn('White')
        self.board['a5'] = Pawn('Black')
        self.board['b6'] = Pawn('Black')
        self.board['e3'] = Pawn('Black')

        self.assertTrue(self.board['c4']
                        ._knight_valid_move(self.board, 'c4', 'd2'))
        self.assertTrue(self.board['c4']
                        ._knight_valid_move(self.board, 'c4', 'd6'))
        self.assertTrue(self.board['c4']
                        ._knight_valid_move(self.board, 'c4', 'a3'))
        self.assertTrue(self.board['c4']
                        ._knight_valid_move(self.board, 'c4', 'a5'))
        self.assertTrue(self.board['c4']
                        ._knight_valid_move(self.board, 'c4', 'b6'))
        self.assertFalse(self.board['c4']
                         ._knight_valid_move(self.board, 'c4', 'b2'))
        self.assertFalse(self.board['c4']
                         ._knight_valid_move(self.board, 'c4', 'e5'))
        self.assertTrue(self.board['c4']
                        ._knight_valid_move(self.board, 'c4', 'e3'))
        self.assertFalse(self.board['c4']
                         ._knight_valid_move(self.board, 'c4', 'c5'))
        self.assertFalse(self.board['c4']
                         ._knight_valid_move(self.board, 'c4', 'c3'))
        self.assertFalse(self.board['c4']
                         ._knight_valid_move(self.board, 'c4', 'b5'))
        self.assertFalse(self.board['c4']
                         ._knight_valid_move(self.board, 'c4', 'h1'))
        self.assertFalse(self.board['c4']
                         ._knight_valid_move(self.board, 'c4', 'c9'))

        self.board['c4'] = ''
        self.board['b2'] = ''
        self.board['e5'] = ''
        self.board['a5'] = ''
        self.board['b6'] = ''
        self.board['e3'] = ''

    def test_bishop_move(self):
        self.board['d4'] = Bishop('White')
        self.board['f6'] = Pawn('Black')
        self.board['b6'] = Pawn('White')
        self.board['b2'] = Pawn('Black')

        self.assertTrue(self.board['d4']
                        ._bishop_valid_move(self.board, 'd4', 'e5'))
        self.assertTrue(self.board['d4']
                        ._bishop_valid_move(self.board, 'd4', 'e3'))
        self.assertTrue(self.board['d4']
                        ._bishop_valid_move(self.board, 'd4', 'b2'))
        self.assertTrue(self.board['d4']
                        ._bishop_valid_move(self.board, 'd4', 'c5'))
        self.assertTrue(self.board['d4']
                        ._bishop_valid_move(self.board, 'd4', 'f6'))
        self.assertTrue(self.board['d4']
                        ._bishop_valid_move(self.board, 'd4', 'f2'))

        self.assertFalse(self.board['d4']
                         ._bishop_valid_move(self.board, 'd4', 'g7'))
        self.assertFalse(self.board['d4']
                         ._bishop_valid_move(self.board, 'd4', 'h8'))
        self.assertFalse(self.board['d4']
                         ._bishop_valid_move(self.board, 'd4', 'bs2'))
        self.assertFalse(self.board['d4']
                         ._bishop_valid_move(self.board, 'd4', 'b6'))
        self.assertFalse(self.board['d4']
                         ._bishop_valid_move(self.board, 'd4', 'a7'))
        self.assertFalse(self.board['d4']
                         ._bishop_valid_move(self.board, 'd4', 'a1'))
        self.assertFalse(self.board['d4']
                         ._bishop_valid_move(self.board, 'd4', 'f7'))

        self.board['d4'] = ''
        self.board['f6'] = ''
        self.board['b6'] = ''
        self.board['b2'] = ''

    def test_queen_move(self):
        self.board['d4'] = Queen('White')
        self.board['d2'] = Pawn('White')
        self.board['d6'] = Pawn('Black')
        self.board['f4'] = Pawn('Black')
        self.board['f6'] = Pawn('White')
        self.board['b6'] = Pawn('Black')
        self.board['b2'] = Pawn('White')

        self.assertTrue(self.board['d4']
                        ._queen_valid_move(self.board, 'd4', 'd5'))
        self.assertTrue(self.board['d4']
                        ._queen_valid_move(self.board, 'd4', 'd3'))
        self.assertTrue(self.board['d4']
                        ._queen_valid_move(self.board, 'd4', 'c4'))
        self.assertTrue(self.board['d4']
                        ._queen_valid_move(self.board, 'd4', 'a4'))
        self.assertTrue(self.board['d4']
                        ._queen_valid_move(self.board, 'd4', 'f4'))
        self.assertTrue(self.board['d4']
                        ._queen_valid_move(self.board, 'd4', 'e5'))
        self.assertTrue(self.board['d4']
                        ._queen_valid_move(self.board, 'd4', 'd6'))
        self.assertTrue(self.board['d4']
                        ._queen_valid_move(self.board, 'd4', 'b6'))

        self.assertFalse(self.board['d4']
                         ._queen_valid_move(self.board, 'd4', 'd2'))
        self.assertFalse(self.board['d4']
                         ._queen_valid_move(self.board, 'd4', 'b2'))
        self.assertFalse(self.board['d4']
                         ._queen_valid_move(self.board, 'd4', 'f6'))
        self.assertFalse(self.board['d4']
                         ._queen_valid_move(self.board, 'd4', 'f7'))
        self.assertFalse(self.board['d4']
                         ._queen_valid_move(self.board, 'd4', 'd8'))
        self.assertFalse(self.board['d4']
                         ._queen_valid_move(self.board, 'd4', 'd1'))
        self.assertFalse(self.board['d4']
                         ._queen_valid_move(self.board, 'd4', 'a1'))
        self.assertFalse(self.board['d4']
                         ._queen_valid_move(self.board, 'd4', 'g1'))
        self.assertFalse(self.board['d4']
                         ._queen_valid_move(self.board, 'd4', 'h5'))

        self.board['d4'] = ''
        self.board['d2'] = ''
        self.board['d6'] = ''
        self.board['f4'] = ''
        self.board['f6'] = ''
        self.board['b6'] = ''
        self.board['b2'] = ''

    def test_king_move(self):
        for index in range(ord('A'), ord('H') + 1):
            position = '{}1'.format(chr(index))
            self.board[position] = ''

        self.board['d5'] = King('Black')

        self.assertTrue(self.board['d5']
                        ._king_valid_move(self.board, 'd5', 'd6'))
        self.assertTrue(self.board['d5']
                        ._king_valid_move(self.board, 'd5', 'e6'))
        self.assertTrue(self.board['d5']
                        ._king_valid_move(self.board, 'd5', 'e5'))
        self.assertTrue(self.board['d5']
                        ._king_valid_move(self.board, 'd5', 'e4'))
        self.assertTrue(self.board['d5']
                        ._king_valid_move(self.board, 'd5', 'd4'))
        self.assertTrue(self.board['d5']
                        ._king_valid_move(self.board, 'd5', 'c4'))
        self.assertTrue(self.board['d5']
                        ._king_valid_move(self.board, 'd5', 'c5'))
        self.assertTrue(self.board['d5']
                        ._king_valid_move(self.board, 'd5', 'c6'))
        self.assertFalse(self.board['d5']
                         ._king_valid_move(self.board, 'd5', 'h6'))

        self.board['e4'] = Pawn('Black')
        self.board['c5'] = Pawn('White')

        self.assertTrue(self.board['d5']
                        ._king_valid_move(self.board, 'd5', 'c5'))
        self.assertFalse(self.board['d5']
                         ._king_valid_move(self.board, 'd5', 'e4'))

        self.board['d5'] = ''
        self.board['e4'] = ''
        self.board['c5'] = ''


class TestSpecialMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        for index in range(ord('A'), ord('H') + 1):
            position = '{}1'.format(chr(index))
            self.board[position] = ''

    def test_castling_move(self):
        self.board['e1'] = King('White')
        self.board['a1'] = Rook('White')
        self.board['h1'] = Rook('White')

        self.assertTrue(self.board
                        ._valid_castling(self.board, 'e1', 'a1'))
        self.assertTrue(self.board
                        ._valid_castling(self.board, 'e1', 'h1'))

        self.board['e1']._moved = True
        self.board['h1']._moved = True

        self.assertFalse(self.board['e1']
                         ._king_valid_move(self.board, 'e1', 'h1'))
        self.assertFalse(self.board['a1']
                         ._rook_valid_move(self.board, 'a1', 'e1'))

        self.board['e1']._moved = False
        self.board['h1']._moved = False

        self.board['f1'] = Queen('White')
        self.assertFalse(self.board
                         ._valid_castling(self.board, 'e1', 'h1'))
        self.assertFalse(self.board['e1']
                         ._king_valid_move(self.board, 'e1', 'h1'))

        self.assertTrue(self.board
                        ._castling_free_way(self.board, 'a1', 'e1'))
        self.assertFalse(self.board
                         ._castling_free_way(self.board, 'h1', 'e1'))

        self.board['e1'] = ''
        self.board['a1'] = ''
        self.board['h1'] = ''
        self.board['f1'] = ''


class TestCheckMate(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board['e8'] = ''
        for index in range(ord('A'), ord('H') + 1):
            position = '{}2'.format(chr(index))
            self.board[position] = ''
            position = '{}1'.format(chr(index))
            self.board[position] = ''

    def test_check(self):
        self.board['D5'] = King('Black')
        self.board['c2'] = Queen('White')

        self.assertFalse(self.board
                         ._is_in_check(self.board, 'Black',
                                       self.board._king_position(self.board,
                                                                 'Black')))

        self.board['d5'] = ''
        self.board['c6'] = King('Black')

        self.assertTrue(self.board
                        ._valid_move(self.board, 'c2', 'c6'))
        self.assertTrue(self.board
                        ._is_in_check(self.board, 'Black',
                                      self.board._king_position(self.board,
                                                                'Black')))

        self.board['c6'] = ''
        self.board['c2'] = ''

    def test_checkmate(self):
        self.board['D5'] = King('Black')
        self.board['c2'] = Queen('White')
        self.board['a4'] = Rook('White')
        self.board['a6'] = Rook('White')

        self.assertFalse(self.board._is_in_checkmate(self.board, 'Black'))

        self.board['d1'] = Rook('White')
        self.board['g3'] = Bishop('White')

        self.assertTrue(self.board
                        ._is_in_checkmate(self.board, 'Black'))

        self.board['c6'] = ''
        self.board['c2'] = ''

    def test_stalemate_checkmate(self):
        for position in ALL_BOARD_POSITIONS:
            self.board[position] = ''
        self.board['D5'] = King('Black')
        self.board['c2'] = Queen('White')
        self.board['a4'] = Rook('White')
        self.board['a6'] = Rook('White')

        self.assertFalse(self.board._is_in_checkmate(self.board, 'Black'))

        self.board['g3'] = Bishop('White')

        self.assertTrue(self.board._is_in_stalemate(self.board, 'Black'))

        self.board['d1'] = Rook('White')

        self.assertTrue(self.board
                        ._is_in_checkmate(self.board, 'Black'))

        self.board['d1'] = ''
        self.board['e4'] = Pawn('White')

        self.assertTrue(self.board._is_in_checkmate(self.board, 'Black'))

        self.board['e4'] = ''
        self.board['c6'] = ''
        self.board['c2'] = ''


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

# if __name__ == '__main__':
#    unittest.main()
