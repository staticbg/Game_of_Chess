import re

from figures import Figure, Pawn, Rook, Knight, Bishop, King, Queen


# TODO: make validations prettier
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

    def castling_free_way(board, origin, target):
        free_way = True
        if ord(origin[0].upper()) > ord(target[0].upper()):
            origin, target = target, origin
        for letter in range(ord(origin[0].upper()) + 1,
                            ord(target[0].upper())):
            if board['{}{}'.format(chr(letter), origin[1])] != '':
                free_way = False
        return free_way

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

    # TODO: en passant special move
    @classmethod
    def pawn_valid_move(cls, board, origin, target):
        if ValidMoves.valid_origin_and_target(origin, target):
            if board[origin]._colour == 'Black' and\
               board[origin]._moved is False and\
               origin[0].upper() == target[0].upper() and\
               int(origin[1]) == int(target[1]) + 2 and\
               board[target] == '' and\
               board['{}{}'.format(target[0], int(target[1]) + 1)] == '':
                return True
            elif board[origin]._colour == 'White' and\
                    board[origin]._moved is False and\
                    origin[0].upper() == target[0].upper() and\
                    int(origin[1]) == int(target[1]) - 2 and\
                    board[target] == '' and\
                    board['{}{}'.format(target[0], int(target[1]) - 1)] == '':
                        return True
            elif board[origin]._colour == 'Black' and\
                    origin[0].upper() == target[0].upper() and\
                    int(origin[1]) == int(target[1]) + 1 and not\
                    isinstance(board[target], Figure):
                        return True
            elif board[origin]._colour == 'White' and\
                    origin[0].upper() == target[0].upper() and\
                    int(origin[1]) == int(target[1]) - 1 and not\
                    isinstance(board[target], Figure):
                        return True
            elif board[origin]._colour == 'Black' and\
                    (target[0].upper() == chr(ord(origin[0].upper()) + 1) or
                     target[0].upper() == chr(ord(origin[0].upper()) - 1)) and\
                    int(origin[1]) == int(target[1]) + 1 and\
                    isinstance(board[target], Figure) and\
                    board[target]._colour != board[origin]._colour:
                        return True
            elif board[origin]._colour == 'White' and\
                    (target[0].upper() == chr(ord(origin[0].upper()) + 1) or
                     target[0].upper() == chr(ord(origin[0].upper()) - 1)) and\
                    int(origin[1]) == int(target[1]) - 1 and\
                    isinstance(board[target], Figure) and\
                    board[target]._colour != board[origin]._colour:
                        return True
            else:
                return False
        else:
            return False

    @classmethod
    def rook_valid_move(cls, board, origin, target):
        if ValidMoves.valid_origin_and_target(origin, target):
            if ValidMoves.can_step_on_target(board, origin, target):
                figure_on_the_way = False
                if target[1] == origin[1] and\
                   ord(origin[0].upper()) < ord(target[0].upper()):
                    origin = '{}{}'.format(chr(ord(origin[0]) + 1), origin[1])
                    while origin[0].upper() != chr(ord(target[0].upper())):
                        if isinstance(board[origin], Figure):
                            figure_on_the_way = True
                            origin = '{}{}'.format(target[0], origin[1])
                        else:
                            origin = '{}{}'\
                                .format(chr(ord(origin[0]) + 1), origin[1])
                elif target[1] == origin[1] and\
                        ord(origin[0].upper()) > ord(target[0].upper()):
                    origin = '{}{}'.format(chr(ord(origin[0]) - 1), origin[1])
                    while origin[0].upper() != chr(ord(target[0].upper())):
                        if isinstance(board[origin], Figure):
                            figure_on_the_way = True
                            origin = '{}{}'.format(target[0], origin[1])
                        else:
                            origin = '{}{}'\
                                .format(chr(ord(origin[0]) - 1), origin[1])
                elif target[0].upper() == origin[0].upper() and\
                        origin[1] < target[1]:
                    origin = '{}{}'.format(origin[0], int(origin[1]) + 1)
                    while int(origin[1]) != int(target[1]):
                        if isinstance(board[origin], Figure):
                            figure_on_the_way = True
                            origin = '{}{}'.format(origin[0], int(target[1]))
                        else:
                            origin = '{}{}'\
                                .format(origin[0], int(origin[1]) + 1)
                elif target[0].upper() == origin[0].upper() and\
                        origin[1] > target[1]:
                    origin = '{}{}'.format(origin[0], int(origin[1]) - 1)
                    while int(origin[1]) != int(target[1]):
                        if isinstance(board[origin], Figure):
                            figure_on_the_way = True
                            origin = '{}{}'.format(origin[0], int(target[1]))
                        else:
                            origin = '{}{}'\
                                .format(origin[0], int(origin[1]) - 1)
                else:
                    figure_on_the_way = True
                return not figure_on_the_way
            elif ValidMoves.valid_castling(board, origin, target):
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def knight_valid_move(cls, board, origin, target):
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

    @classmethod
    def bishop_valid_move(cls, board, origin, target):
        if ValidMoves.valid_origin_and_target(origin, target):
            if ValidMoves.can_step_on_target(board, origin, target):
                figure_on_the_way = False
                if (ord(origin[0].upper()) - ord(target[0].upper())) ==\
                   (int(origin[1]) - int(target[1])) or\
                   (ord(origin[0].upper()) - ord(target[0].upper())) ==\
                   (int(target[1]) - int(origin[1])):
                    if ord(origin[0].upper()) > ord(target[0].upper())\
                       and int(origin[1]) > int(target[1]):
                        origin = '{}{}'.format(chr(ord(origin[0]) - 1),
                                               int(origin[1]) - 1)
                        while origin[0].upper() != chr(ord(target[0].upper())):
                            if isinstance(board[origin], Figure):
                                figure_on_the_way = True
                                origin = '{}{}'.format(target[0], target[1])
                            else:
                                origin = '{}{}'.format(chr(ord(origin[0]) - 1),
                                                       int(origin[1]) - 1)
                    elif ord(origin[0].upper()) < ord(target[0].upper())\
                            and int(origin[1]) > int(target[1]):
                        origin = '{}{}'.format(chr(ord(origin[0]) + 1),
                                               int(origin[1]) - 1)
                        while origin[0].upper() != chr(ord(target[0].upper())):
                            if isinstance(board[origin], Figure):
                                figure_on_the_way = True
                                origin = '{}{}'.format(target[0], target[1])
                            else:
                                origin = '{}{}'.format(chr(ord(origin[0]) + 1),
                                                       int(origin[1]) - 1)
                    elif ord(origin[0].upper()) > ord(target[0].upper())\
                            and int(origin[1]) < int(target[1]):
                        origin = '{}{}'.format(chr(ord(origin[0]) - 1),
                                               int(origin[1]) + 1)
                        while origin[0].upper() != chr(ord(target[0].upper())):
                            if isinstance(board[origin], Figure):
                                figure_on_the_way = True
                                origin = '{}{}'.format(target[0], target[1])
                            else:
                                origin = '{}{}'.format(chr(ord(origin[0]) - 1),
                                                       int(origin[1]) + 1)
                    elif ord(origin[0].upper()) < ord(target[0].upper())\
                            and int(origin[1]) < int(target[1]):
                        origin = '{}{}'.format(chr(ord(origin[0]) + 1),
                                               int(origin[1]) + 1)
                        while origin[0].upper() != chr(ord(target[0].upper())):
                            if isinstance(board[origin], Figure):
                                figure_on_the_way = True
                                origin = '{}{}'.format(target[0], target[1])
                            else:
                                origin = '{}{}'.format(chr(ord(origin[0]) + 1),
                                                       int(origin[1]) + 1)
                    else:
                        figure_on_the_way = True
                    return not figure_on_the_way
                else:
                    return False
            else:
                return False
        else:
            return False

    @classmethod
    def queen_valid_move(cls, board, origin, target):
        return ValidMoves.rook_valid_move(board, origin, target)\
            or ValidMoves.bishop_valid_move(board, origin, target)

    @classmethod
    def king_valid_move(cls, board, origin, target):
        return ValidMoves.valid_origin_and_target(origin, target) and\
            (ValidMoves.valid_castling(board, origin, target) or
             (ValidMoves.can_step_on_target(board, origin, target) and
              ord(origin[0].upper()) - ord(target[0].upper())
              in range(-1, 2) and
              int(origin[1]) - int(target[1]) in range(-1, 2)))

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

    def get_king_position(board, colour):
        for letter in range(ord('A'), ord('H') + 1):
            for index in range(1, 9):
                if isinstance(board['{}{}'.format(chr(letter), index)], King)\
                   and board['{}{}'
                             .format(chr(letter), index)]._colour == colour:
                    return '{}{}'.format(chr(letter), index)

    @classmethod
    def is_in_check(cls, board, colour, king_position):

        king_in_check = False

        for letter in range(ord('A'), ord('H') + 1):
            for index in range(1, 9):
                if isinstance(board['{}{}'.format(chr(letter), index)],
                              Figure) and\
                   board['{}{}'.format(chr(letter), index)]._colour != colour:

                    if ValidMoves.valid_move(board, '{}{}'
                                             .format(chr(letter), index),
                                             king_position):
                        king_in_check = True

        return king_in_check

    @classmethod
    def is_in_checkmate(cls, board, colour):
        king_position = ValidMoves.get_king_position(board, colour)

        valid_king_moves = []

        for letter in range(ord(king_position[0]) - 1,
                            ord(king_position[0]) + 2):
            for index in range(king_position[1] - 1, king_position[1] + 2):
                if ValidMoves.valid_position('{}{}'.format(chr(letter),
                                                           index)) and\
                        ValidMoves.king_valid_move(board, king_position,
                                                   '{}{}'.format(chr(letter),
                                                                 index)):
                            valid_king_moves.append('{}{}'.format(chr(letter),
                                                                  index))

        return all(ValidMoves.is_in_check(board, colour, king_move)
                   for king_move in valid_king_moves)


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
