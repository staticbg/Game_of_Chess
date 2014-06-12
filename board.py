import re

from figures import Figure, Pawn, Rook, Knight, Bishop, King, Queen

from constants import ALL_BOARD_POSITIONS


class Board:
    def __init__(self):
        self._board = [[Rook('Black'), Knight('Black'),
                        Bishop('Black'), Queen('Black'),
                        King('Black'), Bishop('Black'),
                        Knight('Black'), Rook('Black')],
                       [Pawn('Black'), Pawn('Black'),
                        Pawn('Black'), Pawn('Black'),
                        Pawn('Black'), Pawn('Black'),
                        Pawn('Black'), Pawn('Black')],
                       ['']*8, ['']*8, ['']*8, ['']*8,
                       [Pawn('White'), Pawn('White'),
                        Pawn('White'), Pawn('White'),
                        Pawn('White'), Pawn('White'),
                        Pawn('White'), Pawn('White')],
                       [Rook('White'), Knight('White'),
                        Bishop('White'), Queen('White'),
                        King('White'), Bishop('White'),
                        Knight('White'), Rook('White')]]

    def __getitem__(self, position):
        return self._board[8 - int(position[1])][ord(position[0].upper()) - 65]

    def __setitem__(self, position, figure):
        self._board[8 - int(position[1])][ord(position[0].upper()) - 65]\
            = figure

    def __str__(self):
        result = ''
        for index in range(8):
            result = '{}{} '.format(result, 8 - index)
            for symbol in [figure._symbol if isinstance(figure, Figure)
                           else ' ' for figure in self._board[index]]:
                result = '{}|{}'.format(result, symbol)
            result = '{}{}'.format(result, '|\n')
        return '{}{}'.format(result, '   A B C D E F G H')

    def __repr__(self):
        return 'Chess Board'

    def _row(self, position):
        return 8 - int(position[1])

    def _column(self, position):
        return ord(position[0].upper()) - 65

    def _valid_position(self, position):
        return re.match(r'^[a-hA-H][1-8]$', position)

    def _valid_origin_and_target(self, origin, target):
        return self._valid_position(origin) and\
            self._valid_position(target)

    def _can_step_on_target(self, origin, target):
        return isinstance(self._board[self._row(target)]
                                     [self._column(target)], Figure) and\
            self._board[self._row(target)][self._column(target)]._colour !=\
            self._board[self._row(origin)][self._column(origin)]._colour or\
            self._board[self._row(target)][self._column(target)] == ''

    def _valid_move(self, board, origin, target):
        if isinstance(self._board[self._row(origin)]
                                 [self._column(origin)], Pawn):
            return self._board[self._row(origin)][self._column(origin)]\
                       ._pawn_valid_move(board, origin, target)
        elif isinstance(self._board[self._row(origin)]
                                   [self._column(origin)], Rook):
            return self._board[self._row(origin)][self._column(origin)]\
                       ._rook_valid_move(board, origin, target)
        elif isinstance(self._board[self._row(origin)]
                                   [self._column(origin)], Knight):
            return self._board[self._row(origin)][self._column(origin)]\
                       ._knight_valid_move(board, origin, target)
        elif isinstance(self._board[self._row(origin)]
                                   [self._column(origin)], Bishop):
            return self._board[self._row(origin)][self._column(origin)]\
                       ._bishop_valid_move(board, origin, target)
        elif isinstance(self._board[self._row(origin)]
                                   [self._column(origin)], Queen):
            return self._board[self._row(origin)][self._column(origin)]\
                       ._queen_valid_move(board, origin, target)
        elif isinstance(self._board[self._row(origin)]
                                   [self._column(origin)], King):
            return self._board[self._row(origin)][self._column(origin)]\
                       ._king_valid_move(board, origin, target)
        else:
            return False

    def _king_position(self, colour):
        for position in ALL_BOARD_POSITIONS:
            if isinstance(self._board[self._row(position)]
                                     [self._column(position)], King)\
               and self._board[self._row(position)][self._column(position)]\
               ._colour == colour:
                    return position

    def _castling_free_way(self, board, origin, target):
        free_way = True
        if ord(origin[0].upper()) > ord(target[0].upper()):
            origin, target = target, origin
        for letter in range(ord(origin[0].upper()) + 1,
                            ord(target[0].upper())):
            if board['{}{}'.format(chr(letter), origin[1])] != '':
                free_way = False
        return free_way

    def _valid_castling(self, board, origin, target):
        return (origin.upper() == 'E1' and
                (target.upper() == 'H1' or target.upper() == 'A1') or
                target.upper() == 'E1'and
                (origin.upper() == 'H1' or origin.upper() == 'A1') or
                origin.upper() == 'E8' and
                (target.upper() == 'H8' or target.upper() == 'A8') or
                target.upper() == 'E8' and
                (origin.upper() == 'H8' or origin.upper() == 'A8')) and\
               (isinstance(board[origin], King) and
                isinstance(board[target], Rook) or
                isinstance(board[origin], Rook) and
                isinstance(board[target], King)) and\
            board[origin]._colour == board[target]._colour and\
            board[origin]._moved is False and\
            board[target]._moved is False and\
            self._castling_free_way(board, origin, target)

    def _is_king_on_board(self, colour):
        return self._king_position(colour) != []

    def _valid_moves(self, board, colour):
        return ['{}{}'.format(origin, target) for origin in ALL_BOARD_POSITIONS
                for target in ALL_BOARD_POSITIONS
                if self._valid_move(board, origin, target) and
                board[origin]._colour == colour]

    def _all_valid_moves(self, board, colour):
        all_valid_moves = []
        for move in self._valid_moves(board, colour):
            new_board = Board()
            for position in ALL_BOARD_POSITIONS:
                new_board[position] = board[position]
            new_board[move[2:4]], new_board[move[:2]] = new_board[move[:2]], ''
            if not new_board._is_in_check(new_board, colour,
                                          new_board._king_position(colour))\
               and self._is_king_on_board(colour):
                all_valid_moves.append(move)
        return all_valid_moves

    def _is_in_check(self, board, colour, king_position):
        king_in_check = False

        for position in ALL_BOARD_POSITIONS:
            if isinstance(board[position], Figure) and\
               board[position]._colour != colour\
               and self._valid_move(board, position, king_position):
                    king_in_check = True

        return king_in_check

    def _is_in_stalemate(self, board, colour):
        return self._all_valid_moves(board, colour) == []

    def _is_in_checkmate(self, board, colour):
        return board._all_valid_moves(board, colour) == [] and\
            self._is_in_check(board, colour,
                              board._king_position(colour))
