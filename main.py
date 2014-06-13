from multiplayer import MultiPlayer

from constants import ALL_BOARD_POSITIONS


def offers_draw(text):
    return text.upper() == 'DRAW'


def resigns(text):
    return text.upper() == 'RESIGN'


def is_valid_input(text):
    return text.upper() in ALL_BOARD_POSITIONS or\
        offers_draw(text) or resigns(text)


def is_end_game(player_1, player_2, game, origin, target):
    if origin.upper() in ALL_BOARD_POSITIONS and\
        target.upper() in ALL_BOARD_POSITIONS and\
        (game.move(origin, target) == 'Player {} wins'
                                      .format(player_1) or
            game.move(origin, target) == 'Player {} wins'.format(player_2)
            or game.move(origin, target) ==
            'Player {} and Player {} ended the game with a draw'
            .format(player_1, player_2)):
        print(game.move(origin, target))
        return True


def play_game(player_1, player_2, game, game_in_progress=True):
    while game_in_progress:
        print('{} {}'.format(game._player_name(), 'make your move.'))
        print("Select the position of the figure you want to move.")
        origin = input()

        while not is_valid_input(origin):
            print('{}{}'.format('Please enter correct figure position, ',
                                'offer a draw or resign'))
            origin = input()

        if offers_draw(origin):
            draw = game._offer_draw()
            print(draw)
            game_in_progress = (draw == '{} declined'
                                        .format(game._other_player_name()))
        elif resigns(origin):
            game_in_progress = (game._resign() !=
                                '{} wins'.format(game._other_player_name()))
            print(game._resign())
        else:

            print("Select the position to which you want to move the {} on {}"
                  .format(str(game._board[origin]), origin))
            target = input()

            while not is_valid_input(target):
                print("Please enter correct target position")
                target = input()

        game_in_progress = (is_end_game(player_1, player_2,
                                        game, origin, target) is not True)


def start_game():
    print("Enter player 1 (white figures) name")
    player_1 = input()
    print("Enter player 2 (black figures) name")
    player_2 = input()

    if player_1 == '':
        player_1 = '1'
    if player_2 == '':
        player_2 = '2'

    game = MultiPlayer(player_1, player_2)

    play_game(player_1, player_2, game)

if __name__ == "__main__":
    start_game()
