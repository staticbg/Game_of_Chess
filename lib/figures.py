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


class Knight(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._symbol = '\033[3{}mH\033[0m'.format(7*(colour == 'White'))


class Bishop(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._symbol = '\033[3{}mB\033[0m'.format(7*(colour == 'White'))


class Rook(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._moved = False
        self._symbol = '\033[3{}mR\033[0m'.format(7*(colour == 'White'))


class Queen(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._symbol = '\033[3{}mQ\033[0m'.format(7*(colour == 'White'))


class King(Figure):
    def __init__(self, colour):
        self._colour = colour
        self._moved = False
        self._symbol = '\033[3{}mK\033[0m'.format(7*(colour == 'White'))


class LostFigures():
    def __init__(self):
        self._lost_figures = []

    def __eq__(self, other):
        return self._lost_figures == other._lost_figures

    def __str__(self):
        result = ''
        for figure in self._lost_figures:
            result = '{} {}'.format(result, str(figure))
        return result

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self._lost_figures)

    def __getitem__(self, index):
        return self._lost_figures[index]

    def add_figure(self, figure):
        self._lost_figures.append(figure)

    def swap_pawn_for_figure(self, figure):
        self._lost_figures.remove(figure)
        self.add_figure(Pawn(figure._colour))
