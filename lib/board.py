import re

from figures import Figure, Pawn, Rook, Knight, Bishop, King, Queen


class ValidMoves:

    def valid_position(position):
        return re.match(r'^[a-hA-H][1-8]$', position)

    def valid_origin_and_target(origin, target):
        return ValidMoves.valid_position(origin) and\
            ValidMoves.valid_position(target)

    def can_step_on_target(board, origin, target):
        return isinstance(board[target], Figure) and\
            board[target]._colour != board[origin]._colour or\
            board[target] == ''

    def pawn_white_double_forward(board, origin, target):
        return board[origin]._colour == 'White' and\
            board[origin]._moved is False and\
            origin[0].upper() == target[0].upper() and\
            int(origin[1]) == int(target[1]) - 2 and\
            board[target] == '' and\
            board['{}{}'.format(target[0], int(target[1]) - 1)] == ''

    def pawn_black_double_forward(board, origin, target):
        return board[origin]._colour == 'Black' and\
            board[origin]._moved is False and\
            origin[0].upper() == target[0].upper() and\
            int(origin[1]) == int(target[1]) + 2 and\
            board[target] == '' and\
            board['{}{}'.format(target[0], int(target[1]) + 1)] == ''

    def pawn_white_forward(board, origin, target):
        return board[origin]._colour == 'White' and\
            origin[0].upper() == target[0].upper() and\
            int(origin[1]) == int(target[1]) - 1 and not\
            isinstance(board[target], Figure)

    def pawn_black_forward(board, origin, target):
        return board[origin]._colour == 'Black' and\
            origin[0].upper() == target[0].upper() and\
            int(origin[1]) == int(target[1]) + 1 and not\
            isinstance(board[target], Figure)

    def pawn_white_conquer(board, origin, target):
        return board[origin]._colour == 'White' and\
            (target[0].upper() == chr(ord(origin[0].upper()) + 1) or
             target[0].upper() == chr(ord(origin[0].upper()) - 1)) and\
            int(origin[1]) == int(target[1]) - 1 and\
            isinstance(board[target], Figure) and\
            board[target]._colour != board[origin]._colour

    def pawn_black_conquer(board, origin, target):
        return board[origin]._colour == 'Black' and\
            (target[0].upper() == chr(ord(origin[0].upper()) + 1) or
             target[0].upper() == chr(ord(origin[0].upper()) - 1)) and\
            int(origin[1]) == int(target[1]) + 1 and\
            isinstance(board[target], Figure) and\
            board[target]._colour != board[origin]._colour

    # TODO: en passant special move, promotion special move
    @staticmethod
    def pawn_valid_move(board, origin, target):
        return ValidMoves.valid_origin_and_target(origin, target) and\
            (ValidMoves.pawn_white_double_forward(board, origin, target) or
             ValidMoves.pawn_black_double_forward(board, origin, target) or
             ValidMoves.pawn_white_forward(board, origin, target) or
             ValidMoves.pawn_black_forward(board, origin, target) or
             ValidMoves.pawn_white_conquer(board, origin, target) or
             ValidMoves.pawn_black_conquer(board, origin, target))

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

    @staticmethod
    def rook_valid_move(board, origin, target):
        return ValidMoves.valid_origin_and_target(origin, target) and\
            ValidMoves.can_step_on_target(board, origin, target) and\
            (ValidMoves.rook_move_up(board, origin, target) or
             ValidMoves.rook_move_down(board, origin, target) or
             ValidMoves.rook_move_right(board, origin, target) or
             ValidMoves.rook_move_left(board, origin, target))

    @staticmethod
    def knight_valid_move(board, origin, target):
        return ValidMoves.valid_origin_and_target(origin, target) and\
            ValidMoves.can_step_on_target(board, origin, target) and\
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

    @staticmethod
    def bishop_valid_move(board, origin, target):
        return ValidMoves.valid_origin_and_target(origin, target) and\
            ValidMoves.can_step_on_target(board, origin, target) and\
            ValidMoves.bishop_move_diagonal(board, origin, target) and\
            (ValidMoves.bishop_move_up_right(board, origin, target) or
             ValidMoves.bishop_move_up_left(board, origin, target) or
             ValidMoves.bishop_move_down_right(board, origin, target) or
             ValidMoves.bishop_move_down_left(board, origin, target))

    @staticmethod
    def queen_valid_move(board, origin, target):
        return ValidMoves.rook_valid_move(board, origin, target)\
            or ValidMoves.bishop_valid_move(board, origin, target)

    @staticmethod
    def king_valid_move(board, origin, target):
        return ValidMoves.valid_origin_and_target(origin, target) and\
            ValidMoves.can_step_on_target(board, origin, target) and\
            ord(origin[0].upper()) - ord(target[0].upper())\
            in range(-1, 2) and\
            int(origin[1]) - int(target[1]) in range(-1, 2)

    def castling_free_way(board, origin, target):
        free_way = True
        if ord(origin[0].upper()) > ord(target[0].upper()):
            origin, target = target, origin
        for letter in range(ord(origin[0].upper()) + 1,
                            ord(target[0].upper())):
            if board['{}{}'.format(chr(letter), origin[1])] != '':
                free_way = False
        return free_way

    @staticmethod
    def valid_castling(board, origin, target):
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
            ValidMoves.castling_free_way(board, origin, target)

    @staticmethod
    def valid_move(board, origin, target):
        if isinstance(board[origin], Pawn):
            return ValidMoves.pawn_valid_move(board, origin, target)
        elif isinstance(board[origin], Rook):
            return ValidMoves.rook_valid_move(board, origin, target)
        elif isinstance(board[origin], Knight):
            return ValidMoves.knight_valid_move(board, origin, target)
        elif isinstance(board[origin], Bishop):
            return ValidMoves.bishop_valid_move(board, origin, target)
        elif isinstance(board[origin], Queen):
            return ValidMoves.queen_valid_move(board, origin, target)
        elif isinstance(board[origin], King):
            return ValidMoves.king_valid_move(board, origin, target)
        else:
            return False

    # TODO: make it a Board method
    @staticmethod
    def get_king_position(board, colour):
        for letter in range(ord('A'), ord('H') + 1):
            for index in range(1, 9):
                if isinstance(board['{}{}'.format(chr(letter), index)], King)\
                   and board['{}{}'
                             .format(chr(letter), index)]._colour == colour:
                    return '{}{}'.format(chr(letter), index)

    def get_valid_king_moves(board, colour, king_position):
        valid_king_moves = []

        for letter in range(ord(king_position[0]) - 1,
                            ord(king_position[0]) + 2):
            for index in range(int(king_position[1]) - 1,
                               int(king_position[1]) + 2):
                if ValidMoves.valid_position(
                    '{}{}'.format(chr(letter), index)) and\
                    ValidMoves.king_valid_move(
                        board, king_position, '{}{}'.format(chr(letter),
                                                            index)):
                            valid_king_moves.append(
                                '{}{}'.format(chr(letter), index))
        return valid_king_moves

    @staticmethod
    def is_in_check(board, colour, king_position):
        king_in_check = False

        for letter in range(ord('A'), ord('H') + 1):
            for index in range(1, 9):

                if isinstance(
                    board['{}{}'.format(chr(letter), index)], Figure) and\
                   board['{}{}'.format(chr(letter), index)]._colour != colour:

                    if ValidMoves.valid_move(
                        board, '{}{}'.format(chr(letter), index),
                       king_position):
                            king_in_check = True

        return king_in_check

    @staticmethod
    def is_in_checkmate(board, colour):
        valid_king_moves = ValidMoves.get_valid_king_moves(
            board, colour, ValidMoves.get_king_position(board, colour))

        return valid_king_moves != [] and\
            all(ValidMoves.is_in_check(board, colour, king_move)
                for king_move in valid_king_moves) or\
                valid_king_moves == [] and\
                ValidMoves.is_in_check(board, colour, ValidMoves.get_king_position(board, colour))


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
