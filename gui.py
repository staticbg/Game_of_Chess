import pygame

from figures import Figure, Pawn, Rook, Bishop, Queen, King, Knight

from constants import ALL_BOARD_POSITIONS

import multiplayer

import inputbox

pygame.init()
dimension = [1000, 600]
screen = pygame.display.set_mode(dimension)
pygame.display.set_caption('Chess')

board = []
initialized = False

size = 60

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


def menu_window():
    dimension = [1000, 600]
    screen = pygame.display.set_mode(dimension)
    screen.fill(brown)
    pygame.display.set_caption('Enter players names')
    player_1 = inputbox.ask(screen, 'Player 1 name')
    player_2 = inputbox.ask(screen, 'Player 2 name')
    print(player_1, player_2)
    global board
    board = multiplayer.MultiPlayer(player_1, player_2)
    global initialized
    initialized = True
    draw_board()
    pygame.display.flip()


def draw_board():
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

    font = pygame.font.Font(None, 60)
    for letter in range(ord('A'), ord('H') + 1):
        column = font.render(chr(letter), 1, white)
        screen.blit(column, (15 + 60*(letter - 64), 10))
        screen.blit(column, (15 + 60*(letter - 64), 550))
        row = font.render('{}'.format(8 - letter + 65), 1, white)
        screen.blit(row, (25, 15 + 60*(letter - 64)))
        screen.blit(row, (550, 15 + 60*(letter - 64)))

    font = pygame.font.Font(None, 40)
    player_1 = font.render(str(board._player_white), 1, white)
    screen.blit(player_1, (650, 550))
    player_2 = font.render(str(board._player_black), 1, black)
    screen.blit(player_2, (650, 10))


def convert_position(coordinates):
    return '{}{}'.format(chr(64+(coordinates[0]-1)//60),
                         9 - int(coordinates[1]-1)//60)


def win_window(winner):
    dimension = [400, 400]
    screen = pygame.display.set_mode(dimension)
    pygame.display.set_caption('Congratulations {}! You win!'
                               .format(str(winner)))
    win_image = pygame.image.load('./images/You_Win.jpg')
    screen.blit(win_image, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


origin = ''
while True:
    if not initialized:
        menu_window()
    else:
        draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and origin == '':
            origin = convert_position(pygame.mouse.get_pos())
            print('origin', origin)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            target = convert_position(pygame.mouse.get_pos())
            print('target', target)
            if origin in ALL_BOARD_POSITIONS and\
               target in ALL_BOARD_POSITIONS:
                board.move(origin, target)
                if board.move(origin, target) ==\
                        '{} wins'.format(str(board._player_white)) or\
                        board.move(origin, target) ==\
                        '{} wins'.format(str(board._player_black)):
                    win_window(board._other_player_name())
            origin, target = '', ''

pygame.quit()
