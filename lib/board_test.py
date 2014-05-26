import unittest

from figures import Pawn, Knight, Bishop, Rook, Queen, King

from board import Board, ValidMoves


class TestValidMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        for index in range(ord('A'), ord('H') + 1):
            position = '{}2'.format(chr(index))
            self.board[position] = ''

    def test_pawn_move(self):
        self.assertTrue(ValidMoves
                        .pawn_valid_move(self.board, 'A7', 'A6'))
        self.assertTrue(ValidMoves
                        .pawn_valid_move(self.board, 'c7', 'c5'))
        self.assertFalse(ValidMoves
                         .pawn_valid_move(self.board, 'c7', 'd5'))
        self.assertFalse(ValidMoves
                         .pawn_valid_move(self.board, 'cd7', 'csd5'))
        self.assertFalse(ValidMoves
                         .pawn_valid_move(self.board, 'c7', 'c5'))
        self.board['d6'] = Queen('White')
        self.assertTrue(ValidMoves
                        .pawn_valid_move(self.board, 'e7', 'd6'))
        self.board['d6'] = ''

    def test_rook_move(self):
        self.assertTrue(ValidMoves
                        .rook_valid_move(self.board, 'A1', 'a5'))
        self.assertTrue(ValidMoves
                        .rook_valid_move(self.board, 'A1', 'a6'))
        self.assertFalse(ValidMoves
                         .rook_valid_move(self.board, 'A1', 'a7'))
        self.board['a3'] = King('White')
        self.assertFalse(ValidMoves
                         .rook_valid_move(self.board, 'A1', 'a3'))
        self.assertFalse(ValidMoves
                         .rook_valid_move(self.board, 'A1', 'a5'))
        self.board['a2'] = Rook('White')
        self.assertTrue(ValidMoves
                        .rook_valid_move(self.board, 'A2', 'e2'))
        self.assertFalse(ValidMoves
                         .rook_valid_move(self.board, 'A2', 'c4'))
        self.board['a3'] = ''
        self.board['a2'] = ''

    def test_knight_move(self):
        self.board['c4'] = Knight('White')
        self.board['b2'] = Queen('White')
        self.board['e5'] = Pawn('White')
        self.board['a5'] = Pawn('Black')
        self.board['b6'] = Pawn('Black')
        self.board['e3'] = Pawn('Black')

        self.assertTrue(ValidMoves
                        .knight_valid_move(self.board, 'c4', 'd2'))
        self.assertTrue(ValidMoves
                        .knight_valid_move(self.board, 'c4', 'd6'))
        self.assertTrue(ValidMoves
                        .knight_valid_move(self.board, 'c4', 'a3'))
        self.assertTrue(ValidMoves
                        .knight_valid_move(self.board, 'c4', 'a5'))
        self.assertTrue(ValidMoves
                        .knight_valid_move(self.board, 'c4', 'b6'))
        self.assertFalse(ValidMoves
                         .knight_valid_move(self.board, 'c4', 'b2'))
        self.assertFalse(ValidMoves
                         .knight_valid_move(self.board, 'c4', 'e5'))
        self.assertTrue(ValidMoves
                        .knight_valid_move(self.board, 'c4', 'e3'))
        self.assertFalse(ValidMoves
                         .knight_valid_move(self.board, 'c4', 'c5'))
        self.assertFalse(ValidMoves
                         .knight_valid_move(self.board, 'c4', 'c3'))
        self.assertFalse(ValidMoves
                         .knight_valid_move(self.board, 'c4', 'b5'))
        self.assertFalse(ValidMoves
                         .knight_valid_move(self.board, 'c4', 'h1'))
        self.assertFalse(ValidMoves
                         .knight_valid_move(self.board, 'c4', 'c9'))

    def test_bishop_move(self):
        #TODO: write test case scenarios for knight moves
        pass

    def test_queen_move(self):
        #TODO: write test case scenarios for queen moves
        pass

    def test_king_move(self):
        #TODO: write test case scenarios for king moves
        pass


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
