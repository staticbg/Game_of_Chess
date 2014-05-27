from figures import LostFigures


class Player:
    def __init__(self, name):
        self._name = name
        self._lost_figures = LostFigures()

    def __str__(self):
        return 'Player {}'.format(self._name)

    def __repr__(self):
        return self._name
