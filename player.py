class Player:
    def __init__(self, name):
        self._name = name
        self._lost_figures = []

    def __str__(self):
        return 'Player {}'.format(self._name)

    def __repr__(self):
        return self._name

    def add_figure(self, figure):
        self._lost_figures.append(figure)

    def show_lost_figures(self):
        lost_figures = ''
        for figure in self._lost_figures:
            lost_figures = '{} {}'.format(lost_figures, figure)
        return lost_figures
