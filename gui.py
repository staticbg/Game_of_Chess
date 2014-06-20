import pygame

from figures import Figure, Pawn, Rook, Bishop, Queen, King, Knight

from constants import ALL_BOARD_POSITIONS

from multiplayer import MultiPlayer

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
    board = MultiPlayer(player_1, player_2)
    global initialized
    initialized = True
    draw_board()
    pygame.display.flip()


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


def draw_window():
    dimension = [400, 400]
    screen = pygame.display.set_mode(dimension)
    pygame.display.set_caption('Draw')
    draw_image = pygame.image.load('./images/draw.jpg')
    screen.blit(draw_image, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def player_color():
    return white if board._turn == 'White' else black


def draw_promotion_instructions():
    font = pygame.font.Font(None, 30)
    promotion_message_1 =\
        font.render('When pawn is to be promoted', 1, white)
    promotion_message_2 =\
        font.render('enter the name of a figure from:', 1, white)
    promotion_message_3 =\
        font.render('in the console!', 1, white)
    screen.blit(promotion_message_1, (650, 100))
    screen.blit(promotion_message_2, (650, 130))
    screen.blit(promotion_message_3, (650, 200))

    color = int(player_color() == black)
    offset = 0
    for symbol in ['Q', 'B', 'R', 'H']:
        screen.blit(pieces[color][symbol], (650 + offset, 150))
        offset += 60


def draw_draw_offer_buttons():
    font = pygame.font.Font(None, 40)
    background_color = player_color()
    text_color = tuple([255 - background_color[0]]*3)
    resign_button = font.render('No', 1, text_color, background_color)
    screen.blit(resign_button, (800, 350))
    draw_button = font.render('Yes', 1, text_color, background_color)
    screen.blit(draw_button, (700, 350))


def offer_draw():
    draw_draw_offer_buttons()
    global waiting_draw_answer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if mouse_position[0] in range(700, 745) and\
               mouse_position[1] in range(350, 378):
                draw_window()
            elif mouse_position[0] in range(800, 840) and\
                    mouse_position[1] in range(350, 378):
                waiting_draw_answer = False


def draw_player_names():
    font = pygame.font.Font(None, 40)
    player_1 = font.render(str(board._player_white), 1, white)
    screen.blit(player_1, (650, 550))
    player_2 = font.render(str(board._player_black), 1, black)
    screen.blit(player_2, (650, 10))
    player_on_turn = font.render('{}\'s turn'
                                 .format(board._player_name()), 1,
                                 player_color())
    screen.blit(player_on_turn, (650, 250))


def draw_board_rows_and_columns():
    font = pygame.font.Font(None, 60)
    for letter in range(ord('A'), ord('H') + 1):
        column = font.render(chr(letter), 1, white)
        screen.blit(column, (15 + 60*(letter - 64), 10))
        screen.blit(column, (15 + 60*(letter - 64), 550))
        row = font.render('{}'.format(8 - letter + 65), 1, white)
        screen.blit(row, (25, 15 + 60*(letter - 64)))
        screen.blit(row, (550, 15 + 60*(letter - 64)))


def draw_buttons():
    font = pygame.font.Font(None, 40)
    background_color = player_color()
    text_color = tuple([255 - background_color[0]]*3)
    resign_button = font.render('Resign', 1, text_color, background_color)
    screen.blit(resign_button, (800, 290))
    draw_button = font.render('Draw', 1, text_color, background_color)
    screen.blit(draw_button, (700, 290))


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

    draw_promotion_instructions()
    draw_player_names()
    draw_board_rows_and_columns()
    draw_buttons()


def convert_position(coordinates):
    print(coordinates)
    return '{}{}'.format(chr(64+(coordinates[0]-1)//60),
                         9 - int(coordinates[1]-1)//60)


def play_game():
    global origin
    global waiting_draw_answer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and origin == '':
            mouse_position = pygame.mouse.get_pos()
            if mouse_position[0] in range(800, 890) and\
               mouse_position[1] in range(290, 318):
                win_window(board._determine_winner())
            elif mouse_position[0] in range(700, 765) and\
                    mouse_position[1] in range(290, 318):
                waiting_draw_answer = True
            else:
                origin = convert_position(mouse_position)
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
                    win_window(board._determine_winner())
            origin, target = '', ''


origin = ''
waiting_draw_answer = False
while True:
    if not initialized:
        menu_window()
    else:
        draw_board()

    if waiting_draw_answer:
        offer_draw()
        pygame.display.flip()
    else:
        pygame.display.flip()
        play_game()

pygame.quit()
