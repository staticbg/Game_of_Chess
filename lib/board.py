import re

from figures import Figure, Pawn, Rook, Knight, Bishop, King, Queen


#BIG TODO: Fix the isinstance bullshit
class ValidMoves:

    def valid_position(position):
        return re.match(r'^[a-hA-H][1-8]$', position)

    def instance_on_target(board, target, colour):
        return (isinstance(board[target], Figure) and
                board[target]._colour == colour)

    #TODO: pawns can start with a double move..
    @classmethod
    def pawn_valid_move(self, board, origin, target):
        if self.valid_position(origin) and self.valid_position(target):
            if board[origin]._colour == 'Black' and\
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
    def rook_valid_move(self, board, origin, target):
        if self.valid_position(origin) and self.valid_position(target):
            if isinstance(board[target], Figure) and\
               board[target]._colour != board[origin]._colour or\
               board[target] == '':
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
                    while origin[0].upper() != chr(ord(target[0].upper()) + 1):
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
            else:
                return False
        else:
            return False

    @classmethod
    def knight_valid_move(self, board, origin, target):
        if self.valid_position(origin) and self.valid_position(target):
            if isinstance(board[target], Figure) and\
               board[target]._colour != board[origin]._colour or\
               board[target] == '':
                return (target == '{}{}'
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
            else:
                return False
        else:
            return False

    @classmethod
    def bishop_valid_move(self, board, origin, target):
        if self.valid_position(origin) and self.valid_position(target):
            if isinstance(board[target], Figure) and\
               board[target]._colour != board[origin]._colour:
               # TODO: add uggly algorithm
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def queen_valid_move(self, board, origin, target):
        if self.valid_position(origin) and self.valid_position(target):
            if isinstance(board[target], Figure) and\
               board[target]._colour != board[origin]._colour:
               # TODO: add uggly algorithm
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def king_valid_move(self, board, origin, target):
        if self.valid_position(origin) and self.valid_position(target):
            if isinstance(board[target], Figure) and\
               board[target]._colour != board[origin]._colour:
               # TODO: add uggly algorithm
                return True
            else:
                return False
        else:
            return False


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
