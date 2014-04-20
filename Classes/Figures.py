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
        self._symbol = '\033[{}mP\033[0m'.format(30*(colour == 'Black'))


class Knight(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._symbol = '\033[{}mH\033[0m'.format(30*(colour == 'Black'))

class Bishop(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._symbol = '\033[{}mB\033[0m'.format(30*(colour == 'Black'))

class Rook(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._symbol = '\033[{}mR\033[0m'.format(30*(colour == 'Black'))

class Queen(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._symbol = '\033[{}mQ\033[0m'.format(30*(colour == 'Black'))

class King(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._symbol = '\033[{}mK\033[0m'.format(30*(colour == 'Black'))
