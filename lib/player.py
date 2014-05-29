from figures import LostFigures


class Player:
    def __init__(self, name):
        self._name = name
        self._lost_figures = LostFigures()

    def __str__(self):
        return 'Player {}'.format(self._name)

    def __repr__(self):
        return self._name

    def add_figure(self, figure):
        self._lost_figures.add_figure(figure)

    def show_lost_figures(self):
        return str(self._lost_figures)
