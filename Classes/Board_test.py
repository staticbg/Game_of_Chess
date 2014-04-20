import unittest

from Figures import Pawn, Knight, Bishop, Rook, Queen, King

from Board import Board


class TestBoard(unittest.TestCase):
    def test_initialisation(self):
        board = Board()
        self.assertEqual(board[0], [Rook('Black'), Knight('Black'),
                                    Bishop('Black'), King('Black'),
                                    Queen('Black'), Bishop('Black'),
                                    Knight('Black'), Rook('Black')])
        self.assertEqual(board[7], [Rook('White'), Knight('White'),
                                    Bishtop('White'), King('White'),
                                    Queen('White'), Bishop('White'),
                                    Knight('White'), Rook('White')])
        for row in range(1, 7):
            self.assertEqual(board[row], [' ']*8)

    def test_to_string(self):
        board = Board()
        self.assertEqual(str(board), '8 |BlRook|BlKght|BlBish|BlKing|BlQuen|BlKght|BlBish|BlRook|\n'
                                     '7 |BlPawn|BlPawn|BlPawn|BlPawn|BlPawn|BlPawn|BlPawn|BlPawn|\n'
                                     '6 |______|______|______|______|______|______|______|______|\n'
                                     '5 |______|______|______|______|______|______|______|______|\n'
                                     '4 |______|______|______|______|______|______|______|______|\n'
                                     '3 |______|______|______|______|______|______|______|______|\n'
                                     '2 |WhPawn|WhPawn|WhPawn|WhPawn|WhPawn|WhPawn|WhPawn|WhPawn|\n'
                                     '1 |WhRook|WhKght|WhBish|WhKing|WhQuen|WhKght|WhBish|WhRook|')

    
if __name__ == '__main__':
    unittest.main()
