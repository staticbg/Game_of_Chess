import re


def bishop_move_diagonal(board, origin, target):
    return (ord(origin[0].upper()) - ord(target[0].upper())) ==\
        (int(origin[1]) - int(target[1])) or\
        (ord(origin[0].upper()) - ord(target[0].upper())) ==\
        (int(target[1]) - int(origin[1]))


def bishop_move_up_right(board, origin, target):
    figure_on_the_way = True

    if ord(origin[0].upper()) < ord(target[0].upper())\
            and int(origin[1]) < int(target[1]):

        figure_on_the_way = False
        origin = '{}{}'.format(chr(ord(origin[0]) + 1), int(origin[1]) + 1)

        while origin[0].upper() != chr(ord(target[0].upper())):
            if isinstance(board[origin], Figure):
                figure_on_the_way = True
                origin = '{}{}'.format(target[0], target[1])
            else:
                origin = '{}{}'.format(chr(ord(origin[0]) + 1),
                                       int(origin[1]) + 1)
    return not figure_on_the_way


def bishop_move_up_left(board, origin, target):
    figure_on_the_way = True

    if ord(origin[0].upper()) < ord(target[0].upper())\
            and int(origin[1]) > int(target[1]):

        figure_on_the_way = False
        origin = '{}{}'.format(chr(ord(origin[0]) + 1), int(origin[1]) - 1)

        while origin[0].upper() != chr(ord(target[0].upper())):
            if isinstance(board[origin], Figure):
                figure_on_the_way = True
                origin = '{}{}'.format(target[0], target[1])
            else:
                origin = '{}{}'.format(chr(ord(origin[0]) + 1),
                                       int(origin[1]) - 1)
    return not figure_on_the_way


def bishop_move_down_right(board, origin, target):
    figure_on_the_way = True

    if ord(origin[0].upper()) > ord(target[0].upper())\
            and int(origin[1]) < int(target[1]):

        figure_on_the_way = False
        origin = '{}{}'.format(chr(ord(origin[0]) - 1), int(origin[1]) + 1)

        while origin[0].upper() != chr(ord(target[0].upper())):
            if isinstance(board[origin], Figure):
                figure_on_the_way = True
                origin = '{}{}'.format(target[0], target[1])
            else:
                origin = '{}{}'.format(chr(ord(origin[0]) - 1),
                                       int(origin[1]) + 1)
    return not figure_on_the_way


def bishop_move_down_left(board, origin, target):
    figure_on_the_way = True

    if ord(origin[0].upper()) > ord(target[0].upper())\
            and int(origin[1]) > int(target[1]):

        figure_on_the_way = False
        origin = '{}{}'.format(chr(ord(origin[0]) - 1), int(origin[1]) - 1)

        while origin[0].upper() != chr(ord(target[0].upper())):
            if isinstance(board[origin], Figure):
                figure_on_the_way = True
                origin = '{}{}'.format(target[0], target[1])
            else:
                origin = '{}{}'.format(chr(ord(origin[0]) - 1),
                                       int(origin[1]) - 1)
    return not figure_on_the_way


def bishop_valid_move(board, origin, target):
    return bishop_move_diagonal(board, origin, target) and\
        (bishop_move_up_right(board, origin, target) or
         bishop_move_up_left(board, origin, target) or
         bishop_move_down_right(board, origin, target) or
         bishop_move_down_left(board, origin, target))


def rook_move_up(board, origin, target):
    figure_on_the_way = True

    if target[0].upper() == origin[0].upper() and origin[1] < target[1]:

        figure_on_the_way = False
        origin = '{}{}'.format(origin[0], int(origin[1]) + 1)

        while int(origin[1]) != int(target[1]):
            if isinstance(board[origin], Figure):
                figure_on_the_way = True
                origin = '{}{}'.format(origin[0], int(target[1]))
            else:
                origin = '{}{}'.format(origin[0], int(origin[1]) + 1)
    return not figure_on_the_way


def rook_move_down(board, origin, target):
    figure_on_the_way = True

    if target[0].upper() == origin[0].upper() and\
       origin[1] > target[1]:

        figure_on_the_way = False
        origin = '{}{}'.format(origin[0], int(origin[1]) - 1)

        while int(origin[1]) != int(target[1]):
            if isinstance(board[origin], Figure):
                figure_on_the_way = True
                origin = '{}{}'.format(origin[0], int(target[1]))
            else:
                origin = '{}{}'.format(origin[0], int(origin[1]) - 1)
    return not figure_on_the_way


def rook_move_right(board, origin, target):
    figure_on_the_way = True

    if target[1] == origin[1] and\
       ord(origin[0].upper()) < ord(target[0].upper()):

            figure_on_the_way = False
            origin = '{}{}'.format(chr(ord(origin[0]) + 1), origin[1])

            while origin[0].upper() != chr(ord(target[0].upper())):
                if isinstance(board[origin], Figure):
                    figure_on_the_way = True
                    origin = '{}{}'.format(target[0], origin[1])
                else:
                    origin = '{}{}'\
                             .format(chr(ord(origin[0]) + 1), origin[1])
    return not figure_on_the_way


def rook_move_left(board, origin, target):
    figure_on_the_way = True

    if target[1] == origin[1] and\
       ord(origin[0].upper()) > ord(target[0].upper()):

            figure_on_the_way = False
            origin = '{}{}'.format(chr(ord(origin[0]) - 1), origin[1])

            while origin[0].upper() != chr(ord(target[0].upper())):
                if isinstance(board[origin], Figure):
                    figure_on_the_way = True
                    origin = '{}{}'.format(target[0], origin[1])
                else:
                    origin = '{}{}'\
                             .format(chr(ord(origin[0]) - 1), origin[1])
    return not figure_on_the_way


def rook_valid_move(board, origin, target):
    return (rook_move_up(board, origin, target) or
            rook_move_down(board, origin, target) or
            rook_move_right(board, origin, target) or
            rook_move_left(board, origin, target))


class Figure:
    def __init__(self):
        pass

    def __eq__(self, other):
        return (self.__class__.__name__ == other.__class__.__name__ and
                self._colour == other._colour)

    def __str__(self):
        return '{} {}'.format(self._colour, self.__class__.__name__)

    def __repr__(self):
        return str(self)


class Pawn(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._moved = False
        self._symbol = '\033[3{}mP\033[0m'.format(7*(colour == 'White'))

    def _pawn_white_double_forward(self, board, origin, target):
        return int(origin[1]) == 2 and\
            board[origin]._colour == 'White' and\
            board[origin]._moved is False and\
            origin[0].upper() == target[0].upper() and\
            int(origin[1]) == int(target[1]) - 2 and\
            board[target] == '' and\
            board['{}{}'.format(target[0], int(target[1]) - 1)] == ''

    def _pawn_black_double_forward(self, board, origin, target):
        return int(origin[1]) == 7 and\
            board[origin]._colour == 'Black' and\
            board[origin]._moved is False and\
            origin[0].upper() == target[0].upper() and\
            int(origin[1]) == int(target[1]) + 2 and\
            board[target] == '' and\
            board['{}{}'.format(target[0], int(target[1]) + 1)] == ''

    def _pawn_white_forward(self, board, origin, target):
        return board[origin]._colour == 'White' and\
            origin[0].upper() == target[0].upper() and\
            int(origin[1]) == int(target[1]) - 1 and not\
            isinstance(board[target], Figure)

    def _pawn_black_forward(self, board, origin, target):
        return board[origin]._colour == 'Black' and\
            origin[0].upper() == target[0].upper() and\
            int(origin[1]) == int(target[1]) + 1 and not\
            isinstance(board[target], Figure)

    def _pawn_white_conquer(self, board, origin, target):
        return board[origin]._colour == 'White' and\
            (target[0].upper() == chr(ord(origin[0].upper()) + 1) or
             target[0].upper() == chr(ord(origin[0].upper()) - 1)) and\
            int(origin[1]) == int(target[1]) - 1 and\
            isinstance(board[target], Figure) and\
            board[target]._colour != board[origin]._colour

    def _pawn_black_conquer(self, board, origin, target):
        return board[origin]._colour == 'Black' and\
            (target[0].upper() == chr(ord(origin[0].upper()) + 1) or
             target[0].upper() == chr(ord(origin[0].upper()) - 1)) and\
            int(origin[1]) == int(target[1]) + 1 and\
            isinstance(board[target], Figure) and\
            board[target]._colour != board[origin]._colour

    def _pawn_valid_move(self, board, origin, target):
        return board._valid_origin_and_target(origin, target) and\
            (self._pawn_white_double_forward(board, origin, target) or
             self._pawn_black_double_forward(board, origin, target) or
             self._pawn_white_forward(board, origin, target) or
             self._pawn_black_forward(board, origin, target) or
             self._pawn_white_conquer(board, origin, target) or
             self._pawn_black_conquer(board, origin, target))


class Knight(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._symbol = '\033[3{}mH\033[0m'.format(7*(colour == 'White'))

    def _knight_valid_move(self, board, origin, target):
        return board._valid_origin_and_target(origin, target) and\
            board._can_step_on_target(board, origin, target) and\
            (target == '{}{}'
             .format(chr(ord(origin[0]) + 2), int(origin[1]) + 1) or
             target == '{}{}'
             .format(chr(ord(origin[0]) + 2), int(origin[1]) - 1) or
             target == '{}{}'
             .format(chr(ord(origin[0]) - 2), int(origin[1]) + 1) or
             target == '{}{}'
             .format(chr(ord(origin[0]) - 2), int(origin[1]) - 1) or
             target == '{}{}'
             .format(chr(ord(origin[0]) + 1), int(origin[1]) + 2) or
             target == '{}{}'
             .format(chr(ord(origin[0]) + 1), int(origin[1]) - 2) or
             target == '{}{}'
             .format(chr(ord(origin[0]) - 1), int(origin[1]) + 2) or
             target == '{}{}'
             .format(chr(ord(origin[0]) - 1), int(origin[1]) - 2))


class Bishop(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._symbol = '\033[3{}mB\033[0m'.format(7*(colour == 'White'))

    def _bishop_valid_move(self, board, origin, target):
        return board._valid_origin_and_target(origin, target) and\
            board._can_step_on_target(board, origin, target) and\
            bishop_valid_move(board, origin, target)


class Rook(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._moved = False
        self._symbol = '\033[3{}mR\033[0m'.format(7*(colour == 'White'))

    def _rook_valid_move(self, board, origin, target):
        return board._valid_origin_and_target(origin, target) and\
            board._can_step_on_target(board, origin, target) and\
            rook_valid_move(board, origin, target)


class Queen(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._symbol = '\033[3{}mQ\033[0m'.format(7*(colour == 'White'))

    def _queen_valid_move(self, board, origin, target):
        return board._valid_origin_and_target(origin, target) and\
            board._can_step_on_target(board, origin, target) and\
            (rook_valid_move(board, origin, target) or
             bishop_valid_move(board, origin, target))


class King(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._moved = False
        self._symbol = '\033[3{}mK\033[0m'.format(7*(colour == 'White'))

    def _king_valid_move(self, board, origin, target):
        return board._valid_origin_and_target(origin, target) and\
            board._can_step_on_target(board, origin, target) and\
            ord(origin[0].upper()) - ord(target[0].upper())\
            in range(-1, 2) and\
            int(origin[1]) - int(target[1]) in range(-1, 2)
