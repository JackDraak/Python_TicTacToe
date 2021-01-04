# Tic Tac Toe [in Python 3]
# the classic children's game
# Jack Draak 2020

import random


class Cell:
    def __init__(self, value, row, column):
        self.value = str(value)
        self.row = row
        self.column = column
        self.claimed = False

    def set_value(self, value):
        if not self.claimed:
            self.value = str(value)
            self.claimed = True
            return True
        return False

    def is_claimed(self):
        return self.claimed

    def get_value(self):
        return self.value

    def get_position(self):
        return self.row, self.column


def cell_is_claimed(cell):
    for x in range(grid_size):
        for y in range(grid_size):
            if this_game[x][y].get_value() == str(cell) and this_game[x][y].is_claimed():
                return True
    return False


def check_for_winner():
    # select diagonals
    nwse = []
    swne = []
    for i in range(grid_size):
        nwse.append(this_game[i][i])
        swne.append(this_game[abs(i - grid_size + 1)][i])

    win_sets = [nwse, swne]

    # select each column and row
    for x in range(grid_size):
        horizontal = this_game[x]
        vertical = []
        for y in range(grid_size):
            vertical.append(this_game[y][x])

        win_sets.append(vertical)
        win_sets.append(horizontal)

    # # print the 'win_sets'
    # for this_set in win_sets:
    #     for cell in this_set:
    #         print(cell.get_value(), end=", ")
    #     print()

    winner = ""
    winner, block = check_sets(win_sets, winner)
    print(block)  # for Debug
    return winner, block


def check_sets(checkset, winner):
    may_block = 0
    tally_x = 0
    tally_o = 0
    for this_set in checkset:
        tally_x, tally_o = 0, 0
        free, val = free_in_set(this_set)
        if free == 1:
            may_block = val
        for cell in this_set:
            if cell.get_value() == "X":
                tally_x += 1
            elif cell.get_value() == "O":
                tally_o += 1

        if tally_x == grid_size:
            return "X", may_block
        elif tally_o == grid_size:
            return "O", may_block

    if tally_x == grid_size - 1 and tally_o == 0:
        return winner, may_block
    elif tally_o == grid_size - 1 and tally_x == 0:
        return winner, may_block

    return winner, may_block


def claim_cell(cell, player):
    for x in range(grid_size):
        for y in range(grid_size):
            if this_game[x][y].get_value() == str(cell) and not this_game[x][y].is_claimed():
                this_game[x][y].set_value(player)
                return True
    return False


def display(game):
    for x in range(grid_size):
        print("\t", end="")
        for y in range(grid_size):
            print(game[x][y].get_value(), end=" ")
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


def free_in_set(check_set):
    free = 0
    value = str()
    for member in check_set:
        if not member.is_claimed():
            free += 1
            value = member.get_value()
    return free, value


def get_play():
    display(this_game)
    while True:
        this_play = input("select an open cell number: ")
        if this_play.isdigit():
            cell = int(this_play)
            if 0 < cell < grid_size * grid_size + 1:
                if not cell_is_claimed(cell):
                    return cell
        print(this_play + " is not a valid play. Please, ", end="")


def get_player():
    if get_turn_number() % 2 == 0:
        player = "O"
    else:
        player = "X"
    return player


def get_turn_number():
    turn = 1
    for x in range(grid_size):
        for y in range(grid_size):
            if this_game[x][y].is_claimed():
                turn += 1
    print("Turn number: " + str(turn))  # for Debug
    return turn


def init_game(size):
    grid = []
    cell = 1
    for x in range(1, size + 1):
        row = []
        for y in range(1, size + 1):
            row.append(Cell(cell, x, y))
            cell += 1
        grid.append(row)
    return grid


def play_one_player():
    block = 0
    winner = ""
    while not stalemate():
        player = get_player()
        if player == "X" and claim_cell(get_play(), player):
            winner, block = check_for_winner()
            if winner != "":
                print("Game over, " + winner + " won the game.")
                display(this_game)
                break

        elif player == "O":
            if block != 0:
                if claim_cell(block, "O"):
                    winner, block = check_for_winner()
                    if winner != "":
                        print("Game over, " + winner + " won the game.")
                        display(this_game)
                        break

            else:
                o_turn = True
                while o_turn:
                    a_play = random.randint(1, grid_size * grid_size + 1)
                    if claim_cell(a_play, "O"):
                        winner, block = check_for_winner()
                        o_turn = False
                        if winner != "":
                            print("Game over, " + winner + " won the game.")
                            display(this_game)
                            break

    if stalemate() and winner == "":
        print("Game over: stalemate")
        display(this_game)


def play_two_player():
    winner = ""
    while not stalemate():
        player = get_player()
        if claim_cell(get_play(), player):
            winner, block = check_for_winner()
        if winner != "":
            print("Game over, " + winner + " won the game.")
            display(this_game)
            break

    if stalemate() and winner == "":
        print("Game over: stalemate")
        display(this_game)


def stalemate():
    for x in range(grid_size):
        for y in range(grid_size):
            if not this_game[x][y].is_claimed():
                return False
    return True


if __name__ == '__main__':
    grid_size = 3
    while True:
        this_game = init_game(grid_size)

        print()
        intention = input("Would you like to play a two-player game of Tic-Tac-Toe? [<2>, 1, y(es), n(o)] ")

        if intention == "" or intention[0].lower() == "y" or intention[0] == "2":
            play_two_player()
        elif intention[0].lower() == "n" or intention[0] == "1":
            play_one_player()
