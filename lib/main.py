from multiplayer import MultiPlayer


def start_game():
    print("Enter player 1 (white figures) name")
    player_1 = input()
    print("Enter player 2 (black figures) name")
    player_2 = input()
    game = MultiPlayer(player_1, player_2)

    game_in_progress = True
    while game_in_progress:
        print('{} {}'.format(game.get_player_name(), 'make your move.'))
        print("Select the position of the figure you want to move.")
        origin = input()
        print("Select the position to which you want to move the {} on {}"
              .format(str(game._board[origin]), origin))
        target = input()
        if game.move(origin, target) == 'Player {} wins'.format(player_1) or\
           game.move(origin, target) == 'Player {} wins'.format(player_2):
            print(game.move(origin, target))
            game_in_progress = False

if __name__ == "__main__":
    start_game()
