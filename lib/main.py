from multiplayer import MultiPlayer

from constants import ALL_BOARD_POSITIONS


def is_valid_input(text):
    return text.upper() in ALL_BOARD_POSITIONS or\
        text.upper() == 'DRAW' or text.upper() == 'RESIGN'


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

    game_in_progress = True
    while game_in_progress:
        print('{} {}'.format(game.get_player_name(), 'make your move.'))
        print("Select the position of the figure you want to move.")
        origin = input()

        while not is_valid_input(origin):
            print('{}{}'.format('Please enter correct figure position, ',
                                'offer a draw or resign'))
            origin = input()

        print("Select the position to which you want to move the {} on {}"
              .format(str(game._board[origin]), origin))
        target = input()

        while not is_valid_input(target):
            print("Please enter correct target position")
            target = input()

        if origin.upper() in ALL_BOARD_POSITIONS and\
                target.upper() in ALL_BOARD_POSITIONS and\
                game.move(origin, target) == 'Player {} wins'\
                                             .format(player_1) or\
                game.move(origin, target) == 'Player {} wins'.format(player_2)\
                or game.move(origin, target) ==\
                'Player {} and Player {} ended the game with a draw'\
                .format(player_1, player_2):
            print(game.move(origin, target))
            game_in_progress = False


if __name__ == "__main__":
    start_game()
