# Tic Tac Toe [in Python 3]
# the classic children's game
# Jack Draak 2020


def check_for_win(game):
    winner = ""
    players = ["X", "O"]
    winner = check_rows_columns(game, players, winner)
    winner = check_diagonals(game, players, winner)
    winner = check_stalemate(game, winner)
    return winner


def check_diagonals(game, players, winner):
    down = []
    up = []
    for i in range(3):
        down.append(game[i][i])
        up.append(game[abs(i - 2)][i])

    if winner == "":
        winner = check_set_for_win(up, players)
    if winner == "":
        winner = check_set_for_win(down, players)
    return winner


def check_rows_columns(game, players, winner):
    for x in range(3):
        horizontal = game[x]
        vertical = []
        for y in range(3):
            vertical.append(game[y][x])

        if winner == "":
            winner = check_set_for_win(horizontal, players)
        if winner == "":
            winner = check_set_for_win(vertical, players)
    return winner


def check_set_for_win(this_set, players):
    winner = ""
    for player in players:
        if count(player, this_set) == 3:
            winner = player
    return winner


def check_stalemate(game, winner):
    if winner == "":
        if len(game[3]) == 0:
            winner = "stalemate"
    return winner


def count(this, array):
    this_count = 0
    for item in array:
        if item == this:
            this_count += 1
    return this_count


def display(game):
    for x in range(3):
        print("\t", end="")
        for y in range(3):
            print(game[x][y], end=" ")
            if y != 2:
                print(" | ", end=" ")
        if x != 2:
            print()
            print("\t--------------")
    print()


def init_game():
    return [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ]


def play_game():
    game = init_game()
    game_over = False
    while game_over is not True:
        player = player_for(turn_number(game))
        user_turn(player, game)
        winner = check_for_win(game)
        if winner != "":
            print("The winner is: " + winner)
            display(game)
            game_over = True


def player_for(turn):
    if turn % 2 == 0:
        player = "O"
    else:
        player = "X"
    return player


def user_turn(player, game):
    valid_play = False
    while not valid_play:
        display(game)
        this_play = input("Player, " + player + "'s turn. Please enter the number of the cell to claim: ")
        if this_play.isdigit():
            cell = int(this_play)
            if 0 < cell < 10:
                if game[3].__contains__(str(cell)):
                    game[3].remove(str(cell))
                    for row in range(3):
                        for column in range(3):
                            if game[row][column] == str(cell):
                                game[row][column] = player
                                valid_play = True
                else:
                    print("It looks like cell " + str(cell) + " is occupied")


def turn_number(game):
    return 10 - len(game[3])


if __name__ == '__main__':
    play = True
    while play:
        print()
        intention = input("Would you like to play a game of Tic-Tac-Toe? ")
        if intention[0].lower() == "n":
            play = False
        else:
            play_game()
