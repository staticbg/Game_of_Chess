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
                        .pawn_valid_move(self.board, 'A7', 'A6', 'Black'))
        self.assertTrue(ValidMoves
                        .pawn_valid_move(self.board, 'c7', 'c5', 'Black'))
        self.assertFalse(ValidMoves
                         .pawn_valid_move(self.board, 'c7', 'd5', 'Black'))
        self.assertFalse(ValidMoves
                         .pawn_valid_move(self.board, 'cd7', 'csd5', 'Black'))
        self.assertFalse(ValidMoves
                         .pawn_valid_move(self.board, 'c7', 'c5', 'White'))
        self.board['d6'] = Queen('White')
        self.assertTrue(ValidMoves
                        .pawn_valid_move(self.board, 'e7', 'd6', 'Black'))
        self.board['d6'] = ''

    def test_rook_move(self):
        self.assertTrue(ValidMoves
                        .rook_valid_move(self.board, 'A1', 'a5', 'White'))
        self.assertTrue(ValidMoves
                        .rook_valid_move(self.board, 'A1', 'a6', 'White'))
        self.assertFalse(ValidMoves
                         .rook_valid_move(self.board, 'A1', 'a7', 'White'))
        self.board['a3'] = King('White')
        self.assertFalse(ValidMoves
                         .rook_valid_move(self.board, 'A1', 'a3', 'White'))
        self.assertFalse(ValidMoves
                         .rook_valid_move(self.board, 'A1', 'a5', 'White'))
        self.board['a2'] = Rook('White')
        self.assertTrue(ValidMoves
                        .rook_valid_move(self.board, 'A2', 'e2', 'White'))
        self.assertFalse(ValidMoves
                         .rook_valid_move(self.board, 'A2', 'c4', 'White'))
        self.board['a3'] = ''
        self.board['a2'] = ''

    def test_knight_move(self):
        #TODO: write test case scenarios for knight moves
        pass

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
