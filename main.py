# Tic Tac Toe [in Python 3]
# the classic children's game
# Jack Draak 2020

import random


def check_cell(cell, game):
    if game[grid_size].__contains__(str(cell)):
        return True
    else:
        return False


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


def claim_cell(game, player, this_play, valid_play):
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
    return valid_play, game


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
            if grid_size <= 4:
                print("-" * (5 * grid_size))
            elif grid_size <= 7:
                print("-" * (6 * grid_size))
            else:
                print("-" * (7 * grid_size))
    print()


def find_threat():
    return "find threat"


def find_warn():
    return "find warn"


def init_game(size):
    grid = []
    cell = 1
    for x in range(1, size + 1):
        row = []
        for y in range(1, size + 1):
            row.append(str(cell))
            cell += 1
        grid.append(row)
    row = []
    for z in range(1, size * size + 1):
        row.append(str(z))
    grid.append(row)
    return grid


def play_one_player():
    game = init_game(grid_size)
    game_over = False
    while game_over is not True:
        player = player_for(turn_number(game))
        user_turn(player, game)
        winner = check_for_win(game)
        if winner != "":
            print("The winner is: " + winner)
            display(game)
            game_over = True
        else:
            player = player_for(turn_number(game))
            synth_turn(player, game)
            winner = check_for_win(game)
            if winner != "":
                print("The winner is: " + winner)
                display(game)
                game_over = True


def play_two_player():
    game = init_game(grid_size)
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
    print("user turn")
    valid_play = False
    while not valid_play:
        display(game)
        this_play = input("Player, " + player + "'s turn. Please enter the number of the cell to claim: ")
        valid_play, game = claim_cell(game, player, this_play, valid_play)


# TODO: complete synth_turn, presently just a functional copy of user_turn
def synth_turn(player, game):
    print("synth turn")
    winner = ""
    winner = check_stalemate(game, winner)
    if winner != "":
        moved = False
        cell = find_threat(player)
        if cell is not None:
            moved = True
            valid = False
            valid, game = claim_cell(game, player, cell, valid)
        else:
            cell = find_warn(player)
            if cell is not None:
                moved = True
                valid = False
            valid, game = claim_cell(game, player, cell, valid)
        if not moved:
            cell = game[grid_size][random.randint(len(game[grid_size]))]
            valid, game = claim_cell(game, player, cell, valid)
    display(game)


def turn_number(game):
    return (grid_size * grid_size + 1) - len(game[grid_size])


if __name__ == '__main__':
    grid_size = 3  # Ostensibly, allow for games on grids of any size
    while True:
        print()
        intention = input("Would you like to play a two-player game of Tic-Tac-Toe? [<2>, 1, y(es), n(o)] ")
        if intention == "" or intention[0].lower() == "y" or intention[0] == "2":
            play_two_player()
        elif intention[0].lower() == "n" or intention[0] == "1":
            play_one_player()
