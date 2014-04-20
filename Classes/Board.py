from Figures import Figure, Pawn, Rook, Knight, Bishop, King, Queen


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
