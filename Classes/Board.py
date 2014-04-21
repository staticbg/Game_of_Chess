import re

from Figures import Figure, Pawn, Rook, Knight, Bishop, King, Queen


class ValidMoves:

    def valid_position(position):
        return re.match(r'^[a-hA-H][1-8]$', position)

    @classmethod
    def pawn_valid_move(self, board, origin, target, colour):
        if self.valid_position(origin) and self.valid_position(target):
            if target[0] == origin[0] and\
               target[1] == '{}'.format(int(origin[1]) + 1) and\
               board[target] == '':
                return True
            elif target[0] == '{}'.format(chr(ord(origin[0]) + 1)) or\
                    target[0] == '{}'.format(chr(ord(origin[1]) - 1)) and\
                    target[1] == '{}'.format(int(origin[1]) + 1) and\
                    isinstance(board[target], Figure) and\
                    board[target]._colour != colour:
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def rook_valid_move(self, board, origin, target, colour):
        if self.valid_position(origin) and self.valid_position(target):
            if isinstance(board[target], Figure) and\
               board[target]._colour != colour:
                # TODO: add uggly algorithm
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def knight_valid_move(self, board, origin, target, colour):
        if self.valid_position(origin) and self.valid_position(target):
            if isinstance(board[target], Figure) and\
               board[target]._colour != colour:
                return (target == '{}{}'
                        .format(chr(ord(origin[0]) + 2), origin[1] + 1) or
                        target == '{}{}'
                        .format(chr(ord(origin[0]) + 2), origin[1] - 1) or
                        target == '{}{}'
                        .format(chr(ord(origin[0]) - 2), origin[1] + 1) or
                        target == '{}{}'
                        .format(chr(ord(origin[0]) - 2), origin[1] - 1) or
                        target == '{}{}'
                        .format(chr(ord(origin[0]) + 1), origin[1] + 2) or
                        target == '{}{}'
                        .format(chr(ord(origin[0]) + 1), origin[1] - 2) or
                        target == '{}{}'
                        .format(chr(ord(origin[0]) - 1), origin[1] + 2) or
                        target == '{}{}'
                        .format(chr(ord(origin[0]) - 1), origin[1] - 2))
            else:
                return False
        else:
            return False

    @classmethod
    def bishop_valid_move(self, board, origin, target, colour):
        if self.valid_position(origin) and self.valid_position(target):
            if isinstance(board[target], Figure) and\
               board[target]._colour != colour:
               # TODO: add uggly algorithm
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def queen_valid_move(self, board, origin, target, colour):
        if self.valid_position(origin) and self.valid_position(target):
            if isinstance(board[target], Figure) and\
               board[target]._colour != colour:
               # TODO: add uggly algorithm
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def king_valid_move(self, board, origin, target, colour):
        if self.valid_position(origin) and self.valid_position(target):
            if isinstance(board[target], Figure) and\
               board[target]._colour != colour:
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
