from Figures import Figure, Pawn, Rook, Knight, Bishop, King, Queen


class ValidMoves:

    @classmethod
    def pawn_valid_move(self, board, start, end, colour):
        if start[0] not in range(1, 9) or\
           start[1] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] or\
           end[0] not in range(1, 9) or\
           end[1] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            return False
        if board[8 - start[0]][ord(start[1]) - 65] == Pawn(colour):
            if end == [start[0] + 1, start[1]]\
               and board[8 - end[0]][ord(end[1]) - 65] == '':
                return True
            elif (end == [start[0] + 1, chr(ord(start[1]) - 1)] or
                  end == [start[0] + 1, chr(ord(start[1]) + 1)] and
                  isinstance(board[8 - end[0]][ord(end[1]) - 65], Figure) and
                  board[8 - end[0]][ord(end[1]) - 65]._colour != colour):
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

    def __getitem__(self, index):
        return self._board[index]

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
