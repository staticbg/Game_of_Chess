from board import Board, ValidMoves

from figures import Figure, Pawn, Rook, Bishop, Knight, Queen, King

from player import Player


class Game:

    def __init__(self, player_1, player_2):
        self._board = Board()
        self._player_white = player_1
        self._player_black = player_2
        self._turn = 'White'
        print(str(self._board))

    def next_turn(self):
        if self._turn == 'White':
            self._turn = 'Black'
        else:
            self._turn = 'White'

    def move(self, origin, target):
        if ValidMoves.is_in_checkmate(self._board, self._turn):
            self.next_turn()
            return 'Player {} wins'.format(self._turn)
        elif isinstance(self._board[origin], Figure) and\
                self._board[origin]._colour == self._turn:
            if ValidMoves.valid_move(self._board, origin, target):
                self._board[target] = self._board[origin]
                temp_origin = self._board[origin]
                self._board[origin] = ''
                if ValidMoves\
                   .is_in_check(self._board, self._turn,
                                ValidMoves.get_king_position(self._board,
                                                             self._turn)):
                    print("Not a valid move, your King is checked.")
                    self._board[origin] = self._board[target]
                    self._board[origin] = temp_origin
                    self.next_turn()
                self.next_turn()
            elif ValidMoves.valid_castling(self._board, origin, target):
                if origin[0].upper() == 'A' or target[0].upper() == 'A':
                    self._board['d{}'.format(origin[1])]\
                        = Rook(self._board[origin]._colour)
                    self._board['c{}'.format(origin[1])]\
                        = King(self._board[origin]._colour)
                else:
                    self._board['f{}'.format(origin[1])]\
                        = Rook(self._board[origin]._colour)
                    self._board['g{}'.format(origin[1])]\
                        = King(self._board[origin]._colour)
                self._board[origin], self._board[target] = '', ''
            else:
                return "Not a valid move, please try again!"
        else:
            return "Not a valid move, please try again!"
        print(str(self._board))
