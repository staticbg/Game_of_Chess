from board import Board

from figures import Figure, Pawn, Rook, Bishop, Knight, Queen, King

from player import Player


class MultiPlayer:

    def __init__(self, player_1='Player 1', player_2='Player 2'):
        self._board = Board()
        self._player_white = Player(player_1)
        self._player_black = Player(player_2)
        self._turn = 'White'
        print(str(self._board))

    def _player_name(self):
        return str(self._player_white) * (self._turn == 'White') +\
            str(self._player_black) * (self._turn == 'Black')

    def _other_player_name(self):
        return str(self._player_white) * (self._turn == 'Black') +\
            str(self._player_black) * (self._turn == 'White')

    def _offer_draw(self):
        print("{} offers a draw. y/n".format(self._player_name()))
        answer = input()
        if answer.upper() == 'Y':
            return '{} and {} ended the game with a draw'\
                   .format(str(self._player_white), str(self._player_black))
        elif answer.upper() == 'N':
            return '{} declined'.format(self._other_player_name())
        else:
            print("Please give your answer: y/n")
            return self._offer_draw()

    def _resign(self):
        return '{} wins'.format(self._other_player_name())

    def _next_turn(self):
        self._turn = 'Black' * (self._turn == 'White') +\
                     'White' * (self._turn == 'Black')

    def _capture(self, position):
        if self._turn == 'White':
            self._player_black.add_figure(self._board[position])
        else:
            self._player_white.add_figure(self._board[position])

    def _is_pawn_on_end(self, board, target):
        return isinstance(self._board[target], Pawn) and\
            int(target[1]) == 1 + 7 * (self._turn == board[target]._colour)

    def _promote_pawn(self):
        promotion = {'QUEEN': Queen, 'BISHOP': Bishop,
                     'ROOK': Rook, 'KNIGHT': Knight}

        promoted_pawn = input()
        if promoted_pawn.upper() in ['QUEEN', 'BISHOP', 'ROOK', 'KNIGHT']:
            return promotion[promoted_pawn.upper()]
        else:
            print("Please choose between queen, bishop, rook and knight")
            return self._promote_pawn()

    def _make_castling(self, origin, target):
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
        self._next_turn()

    def _king_is_in_check(self):
        return self._board._is_in_check(self._board, self._turn,
                                        self._board
                                        ._king_position(self._board,
                                                        self._turn))

    def _move_figure(self, origin, target):
        if isinstance(self._board[target], Figure):
                self._capture(target)

        self._board[target] = self._board[origin]
        temp_origin = self._board[origin]
        self._board[origin] = ''

        if self._king_is_in_check():
            self._board[origin] = self._board[target]
            self._board[origin] = temp_origin
            self._next_turn()
            return "Not a valid move, your King is checked."

        if self._is_pawn_on_end(self._board, target):
            self._board[target] = self._promote_pawn()(self._turn)
        self._next_turn()

    def _validate_and_move_figure(self, origin, target):
        if self._board._valid_move(self._board, origin, target):
            self._move_figure(origin, target)

        elif self._board._valid_castling(self._board, origin, target):
            self._make_castling(origin, target)

        else:
            print(str(self._board))
            return "Not a valid move, please try again!"

    def _determine_winner(self):
        winner = str(self._player_white) * (self._turn == 'Black') +\
            str(self._player_black) * (self._turn == 'White')
        return '{} wins'.format(winner)

    def move(self, origin, target):
        if self._board._is_in_checkmate(self._board, self._turn):
            return self._determine_winner()

        elif self._board._is_in_stalemate(self._board, self._turn):
            return '{} and {} ended the game with a draw'\
                   .format(str(self._player_white), str(self._player_black))

        elif isinstance(self._board[origin], Figure) and\
                self._board[origin]._colour == self._turn:
            if self._validate_and_move_figure(origin, target) is not None:
                return self._validate_and_move_figure(origin, target)

        else:
            return "Not a valid move, please try again!"
            print(str(self._board))

        print(str(self._board))
