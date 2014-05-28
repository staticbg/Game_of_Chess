from board import Board, ValidMoves

from figures import Figure, Pawn, Rook, Bishop, Knight, Queen, King

from player import Player


class Game:

    def __init__(self, player_1='Player 1', player_2='Player 2'):
        self._board = Board()
        self._player_white = player_1
        self._player_black = player_2
        self._turn = 'White'
        print(str(self._board))

    def next_turn(self):
        self._turn = 'Black' * (self._turn == 'White') +\
                     'White' * (self._turn == 'Black')

    def is_pawn_on_end(self, board, target, colour):
        return isinstance(self._board[target], Pawn) and\
            int(target[1]) == 1 + 7 * (colour == board[target]._colour)

    def promote_pawn(self):
        promotion = {'QUEEN': Queen, 'BISHOP': Bishop,
                     'ROOK': Rook, 'KNIGHT': Knight}

        promoted_pawn = input()
        if promoted_pawn.upper() in ['QUEEN', 'BISHOP', 'ROOK', 'KNIGHT']:
            return promotion[promoted_pawn.upper()]
        else:
            print("Please choose between queen, bishop, rook and knight")
            return self.promote_pawn()

    def make_castling(self, origin, target):
        if origin[0].upper() == 'A' or target[0].upper() == 'A':
            self._board['d{}'.format(origin[1])] =\
                Rook(self._board[origin]._colour)
            self._board['c{}'.format(origin[1])] =\
                King(self._board[origin]._colour)

        else:
            self._board['f{}'.format(origin[1])] =\
                Rook(self._board[origin]._colour)
            self._board['g{}'.format(origin[1])] =\
                King(self._board[origin]._colour)

        self._board[origin], self._board[target] = '', ''
        self.next_turn()

    def king_is_in_check(self):
        return ValidMoves.is_in_check(self._board, self._turn,
                                      ValidMoves.get_king_position(self._board,
                                                                   self._turn))

    def move(self, origin, target):
        if ValidMoves.is_in_checkmate(self._board, self._turn):
            winner = str(self._player_white) * (self._turn == 'Black') +\
                str(self._player_black) * (self._turn == 'White')
            return '{} wins'.format(winner)

        elif isinstance(self._board[origin], Figure) and\
                self._board[origin]._colour == self._turn:

            if ValidMoves.valid_move(self._board, origin, target):

                self._board[target] = self._board[origin]
                temp_origin = self._board[origin]
                self._board[origin] = ''

                if self.king_is_in_check():
                    print("Not a valid move, your King is checked.")
                    self._board[origin] = self._board[target]
                    self._board[origin] = temp_origin
                    self.next_turn()

                if self.is_pawn_on_end(self._board, target, self._turn):
                    self._board[target] = self.promote_pawn()(self._turn)
                self.next_turn()

            elif ValidMoves.valid_castling(self._board, origin, target):
                self.make_castling(origin, target)

            else:
                return "Not a valid move, please try again!"
                print(str(self._board))

        else:
            return "Not a valid move, please try again!"
            print(str(self._board))

        print(str(self._board))
