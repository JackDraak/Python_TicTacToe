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
    for i in range(grid_size):
        down.append(game[i][i])
        up.append(game[abs(i - grid_size + 1)][i])

    if winner == "":
        winner = check_set_for_win(up, players)
    if winner == "":
        winner = check_set_for_win(down, players)
    return winner


def check_rows_columns(game, players, winner):
    for x in range(grid_size):
        horizontal = game[x]
        vertical = []
        for y in range(grid_size):
            vertical.append(game[y][x])

        if winner == "":
            winner = check_set_for_win(horizontal, players)
        if winner == "":
            winner = check_set_for_win(vertical, players)
    return winner


def check_set_for_win(this_set, players):
    winner = ""
    for player in players:
        if count(player, this_set) == grid_size:
            winner = player
    return winner


def check_stalemate(game, winner):
    if winner == "":
        if len(game[grid_size]) == 0:
            winner = "stalemate"
    return winner


def count(this, array):
    this_count = 0
    for item in array:
        if item == this:
            this_count += 1
    return this_count


def display(game):
    for x in range(grid_size):
        print("\t", end="")
        for y in range(grid_size):
            print(game[x][y], end=" ")
            if y != grid_size - 1:
                print(" | ", end=" ")
        if x != grid_size - 1:
            print()
            print("\t", end="")
            print("-" * (6 * grid_size))
    print()


def init_game():
    grid = []
    cell = 1
    for x in range(1, grid_size + 1):
        row = []
        for y in range(1, grid_size + 1):
            row.append(str(cell))
            cell += 1
        grid.append(row)
    row = []
    for z in range(1, grid_size * grid_size + 1):
        row.append(str(z))
    grid.append(row)
    return grid


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
            if 0 < cell < grid_size * grid_size + 1:
                if game[grid_size].__contains__(str(cell)):
                    game[grid_size].remove(str(cell))
                    for row in range(grid_size):
                        for column in range(grid_size):
                            if game[row][column] == str(cell):
                                game[row][column] = player
                                valid_play = True
                else:
                    print("It looks like cell " + str(cell) + " is occupied")


def turn_number(game):
    return (grid_size * grid_size + 1) - len(game[grid_size])


if __name__ == '__main__':
    grid_size = 3  # Ostensibly, allow for games on boards sized 5x5, 7x7, etc...
    play = True
    while play:
        print()
        intention = input("Would you like to play a game of Tic-Tac-Toe? ")
        if intention[0].lower() == "n":
            play = False
        else:
            play_game()
