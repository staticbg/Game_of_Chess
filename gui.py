import pygame

from figures import Figure, Pawn, Rook, Bishop, Queen, King, Knight

import multiplayer

pygame.init()
dimension = [600, 600]
screen = pygame.display.set_mode(dimension)
pygame.display.set_caption("Chess")

size = 60

end = False

board = multiplayer.MultiPlayer()

black = (0, 0, 0)
white = (255, 255, 255)
brown = (161, 103, 11)

pieces = [{}, {}]
pieces[0]['P'] = pygame.image.load('./images/white_pawn.png')
pieces[0]['R'] = pygame.image.load('./images/white_rook.png')
pieces[0]['B'] = pygame.image.load('./images/white_bishop.png')
pieces[0]['H'] = pygame.image.load('./images/white_knight.png')
pieces[0]['K'] = pygame.image.load('./images/white_king.png')
pieces[0]['Q'] = pygame.image.load('./images/white_queen.png')
pieces[1]['P'] = pygame.image.load('./images/black_pawn.png')
pieces[1]['R'] = pygame.image.load('./images/black_rook.png')
pieces[1]['B'] = pygame.image.load('./images/black_bishop.png')
pieces[1]['H'] = pygame.image.load('./images/black_knight.png')
pieces[1]['K'] = pygame.image.load('./images/black_king.png')
pieces[1]['Q'] = pygame.image.load('./images/black_queen.png')


def is_light(row, column):
    return white if (row % 2) == (column % 2) else black


def is_figure(row, column):
    return isinstance(board._board['{}{}'.format(chr(column + 65), 8 - row)],
                      Figure)


def figure_colour(row, column):
    return 0 if board._board['{}{}'.format(chr(column + 65), 8 - row)]\
                     ._colour == 'White' else 1


def set_figure(row, column):
    colour = figure_colour(row, column)
    if isinstance(board._board['{}{}'.format(chr(column + 65), 8 - row)],
                  Pawn):
        symbol = 'P'
    elif isinstance(board._board['{}{}'.format(chr(column + 65), 8 - row)],
                    Bishop):
        symbol = 'B'
    elif isinstance(board._board['{}{}'.format(chr(column + 65), 8 - row)],
                    Rook):
        symbol = 'R'
    elif isinstance(board._board['{}{}'.format(chr(column + 65), 8 - row)],
                    Knight):
        symbol = 'H'
    elif isinstance(board._board['{}{}'.format(chr(column + 65), 8 - row)],
                    King):
        symbol = 'K'
    elif isinstance(board._board['{}{}'.format(chr(column + 65), 8 - row)],
                    Queen):
        symbol = 'Q'
    screen.blit(pieces[colour][symbol], (65+column*60, 65+row*60))


def draw_board(board):

    screen.fill(brown)
    for row in range(8):
        for column in range(8):
            pygame.draw.rect(screen,
                             is_light(row, column),
                             [size*(column + 1),
                              size*(row + 1),
                              size,
                              size])
            if is_figure(row, column):
                set_figure(row, column)


while True:
    draw_board(board)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

pygame.quit()
