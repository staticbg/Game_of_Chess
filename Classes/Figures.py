class Figure:
    def __init__(self):
        pass

    def __eq__(self, other):
        return (self.__class__.__name__ == other.__class__.__name__ and
                self._colour == other._colour)

    def __str__(self):
        return '{} {}'.format(self._colour, self.__class__.__name__)

    def __repr__(self):
        return self.str()


class Pawn(Figure):
    def __init__(self, colour):
        self._colour = colour


class Knight(Figure):
    def __init__(self, colour):
        self._colour = colour


class Bishop(Figure):
    def __init__(self, colour):
        self._colour = colour


class Rook(Figure):
    def __init__(self, colour):
        self._colour = colour


class Queen(Figure):
    def __init__(self, colour):
        self._colour = colour


class King(Figure):
    def __init__(self, colour):
        self._colour = colour
